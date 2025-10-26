# Imports
from db.mongoClient import getDb
from bson.objectid import ObjectId

def createMessage(data: dict):
    """
    Create a new message in database

    :param data: message data dictionary

    :return: insert result
    """

    # Get database instance
    db = getDb()

    # Get message collection
    collection = db.get_collection('message')

    # Insert new message and return result
    result = collection.insert_one(data)
    return result


def getMessages(receiver: str) -> list:
    """
    Busca todas as mensagens não lidas para um destinatário específico.

    :param receiver: username do destinatário ('to' field).
    :return: Uma lista de documentos de mensagem (dicionários).
    """
    db = getDB()
    collection = db.get_collection('Message')

    # Query: Busca mensagens onde 'to' é o receiver E 'status' é 'unread'
    query = {
        "to": receiver,
        "status": "unread"
    }

    # Retorna as mensagens como uma lista
    messages = list(collection.find(query))
    return messages


def updateMessageStatus(message_ids: list, status: str) -> int:
    """
    Atualiza o status de uma lista de mensagens.

    :param message_ids: Uma lista de _id's das mensagens (strings ou ObjectId) a serem atualizadas.
    :param status: O novo status ('read' ou 'unread').
    :return: O número de documentos modificados.
    """
    db = getDB()
    collection = db.get_collection('Message')

    # Converte os IDs para ObjectId, necessário para buscas no MongoDB
    object_ids = [ObjectId(id) for id in message_ids]

    # Query: Encontra todos os documentos onde o _id está na lista fornecida
    query = {
        "_id": {"$in": object_ids}
    }

    # Update: Define o campo 'status' para o novo valor
    update_op = {
        "$set": {"status": status}
    }

    result = collection.update_many(query, update_op)
    return result.modified_count