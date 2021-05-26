import time

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


from data import load_data, violin
from utils import get_logger, prompt


logger = get_logger()


if __name__ == "__main__":
    data = load_data("query_1621408997.07960f_startable.txt")

    # uncomment to draw violin plot
    # violin(data)

    # split training and test data
    train_size = 0.1
    test_size = 0.1
    logger.info(f"Use {train_size} of all data for training.")
    logger.info(f"Use {test_size} of all data for test.")
    train_data, test_data, train_label, test_label = train_test_split(
        data.loc[:, "I": "A_1"], data["Type"],
        random_state=1,
        train_size=train_size,
        test_size=test_size)

    # scale data
    scaler = StandardScaler()
    train_data = scaler.fit_transform(train_data)
    test_data = scaler.transform(test_data)

    # fit C-SVM model
    logger.info(prompt("BEGIN: fit C-SVM model"))
    logger.info("Fitting C-SVM model...")
    model = SVC(gamma="auto")
    end = time.time()
    model.fit(X=train_data, y=train_label)
    logger.info(f"Model fitted, time {time.time()-end:.1f} s")
    logger.info(prompt("END: fit C-SVM model"))

    # test C-SVM model
    logger.info(prompt("BEGIN: test C-SVM model"))
    logger.info("Testing C-SVM model...")
    end = time.time()
    train_pred = model.predict(train_data)
    train_score = accuracy_score(train_label, train_pred)
    train_confusion = confusion_matrix(train_label, train_pred)
    logger.info(f"Tested on train data ({time.time()-end:.1f} s)")
    logger.info(f"Training acc {train_score:.4f}, confusion matrix:\n" + str(train_confusion))

    end = time.time()
    test_pred = model.predict(test_data)
    test_score = accuracy_score(test_label, test_pred)
    test_confusion = confusion_matrix(test_label, test_pred)
    logger.info(f"Tested on test data ({time.time()-end:.1f} s), , time ")
    logger.info(f"Test acc {test_score:.4f}, confusion matrix:\n" + str(test_confusion))
    logger.info(prompt("END: test C-SVM model"))
