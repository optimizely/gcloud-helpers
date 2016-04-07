from gcloud import datastore
from gcloud.datastore import SCOPE
from gcloud.datastore.connection import Connection

from oauth2client import service_account

def get_connection(client_email, private_key_string):
  svc_account_credentials = service_account.ServiceAccountCredentials._from_p12_keyfile_contents(
    service_account_email=client_email,
    private_key_pkcs12=private_key_string,
    scopes=SCOPE)

  return Connection(credentials=svc_account_credentials)


def connect_to_dataset(dataset_id, client_email, private_key_string):
  connection = get_connection(client_email, private_key_string)
  datastore.set_default_connection(connection)
  datastore.set_default_dataset_id(dataset_id)

