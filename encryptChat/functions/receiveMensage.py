from utils.criptography.criptography import Crypto
# Assumindo que a chave é carregada do constants.py
from utils.constants import ENCRYPTION_KEY
from models.message import getMessages
from models.message import updateMessageStatus


def receiveMessage(receiver: str, mark_as_read: bool = True) -> list:
    """
    Recebe mensagens não lidas para um usuário, as descriptografa
    e opcionalmente as marca como lidas.

    :param receiver: username do usuário que está recebendo as mensagens.
    :param mark_as_read: (opcional) Se deve marcar as mensagens como "read" no banco de dados. Padrão: True.
    :return: Uma lista de dicionários contendo as mensagens descriptografadas.
    """
    try:
        # Inicializa o objeto Crypto com a mesma chave usada para criptografar
        crypto = Crypto(key=ENCRYPTION_KEY)

        # 1. Busca as mensagens não lidas
        unread_messages = getMessages(receiver)
        print(unread_messages)
        received_messages = []
        message_ids_to_update = []

        for msg_doc in unread_messages:
            print(unread_messages)
            encrypted_msg = msg_doc['message']

            # 2. Descriptografa a mensagem
            # Fernet.decrypt retorna bytes, então decodificamos para string
            decrypted_msg_bytes = crypto.decrypt(encrypted_msg)
            decrypted_msg = decrypted_msg_bytes.decode('utf-8')

            # 3. Adiciona a mensagem descriptografada à lista de retorno
            received_messages.append({
                'sender': msg_doc['from'],
                'message': decrypted_msg,
                'timestamp': msg_doc.get('timestamp')  # Se você armazenar timestamp
            })

            # Armazena o ID da mensagem para a atualização de status
            # É importante garantir que seja um valor que possa ser convertido para ObjectId
            message_ids_to_update.append(msg_doc['_id'])

        # 4. Opcional: Marca as mensagens como lidas no banco de dados
        if mark_as_read and message_ids_to_update:
            updateMessageStatus(message_ids_to_update, 'read')

        return received_messages

    except Exception as e:
        # Captura e levanta o erro, útil para debugging
        raise Exception(f"Failed to receive/decrypt messages for {receiver}. Error: {e}")
