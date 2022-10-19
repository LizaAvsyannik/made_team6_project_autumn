from bertopic import BERTopic

def classify_article(path_to_model: str, abstract: str):
    topic_model = BERTopic.load(path_to_model)
    topic = topic_model.transform([abstract])
    topic = topic_model.topic_labels_[topic[0][0]]
    return topic
