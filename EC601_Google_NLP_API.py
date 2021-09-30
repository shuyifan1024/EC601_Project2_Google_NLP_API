#This code comes from the example given by Google.  
#Because this homework is to learn to call API, so I use the teaching code given by Google.
from google.cloud import language_v1

def sample_analyze_sentiment(gcs_content_uri):

    client = language_v1.LanguageServiceClient()

    gcs_content_uri ='cloud-ml-data/NL-classification/happiness.csv' 

    
    type_ = language_v1.Document.Type.PLAIN_TEXT

    
    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type_": type_, "language": language}

    
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))


    print(u"Language of the text: {}".format(response.language))



def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gcs_content_uri",
        type=str,
        default="gs://cloud-samples-data/language/sentiment-positive.txt",
    )
    args = parser.parse_args()

    sample_analyze_sentiment(args.gcs_content_uri)


if __name__ == "__main__":
    main()