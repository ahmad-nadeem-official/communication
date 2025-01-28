# Chat Application Documentation

## 🚀 Project Overview
This project demonstrates a simple client-server chat application built using Python's `socket` and `threading` libraries. The application allows multiple clients to connect to a server and communicate with each other in real-time.

---

## 📁 File Structure

```plaintext
├── mian.py   # Client-side implementation
└── server.py # Server-side implementation
```

---

## 🔧 Requirements
- Python 3.x

To install required dependencies, use:
```bash
pip install -r requirements.txt
```
_Note: No external libraries are required for this project._

---

## 🛠️ How to Run

### **1. Start the Server**
Run the following command in your terminal to start the server:
```bash
python server.py
```
The server will start listening for incoming connections.

### **2. Start the Client**
Open another terminal and run:
```bash
python mian.py
```
You will be prompted to choose a nickname:
```plaintext
Choose your nickname: Batman
```
After entering your nickname, you can start sending messages.

---

## 📜 Code Explanation

### **Server (`server.py`)**

#### **Configuration**
```python
HOST = socket.gethostbyname(socket.gethostname())  # Localhost
PORT = 12345        # Port to listen on
```
The server binds to the host IP address and port 12345 to listen for incoming connections.

#### **Key Functions**
- **Broadcast Messages**: Sends messages to all connected clients.
  ```python
  def broadcast(message):
      for client in clients:
          client.send(message)
  ```
- **Handle Individual Clients**: Listens for incoming messages from a specific client and handles disconnections.
  ```python
  def handle_client(client):
      while True:
          try:
              message = client.recv(1024)
              broadcast(message)
          except:
              index = clients.index(client)
              clients.remove(client)
              client.close()
              nickname = nicknames[index]
              broadcast(f'{nickname} has left the chat.'.encode('utf-8'))
              nicknames.remove(nickname)
              break
  ```
- **Accept New Connections**: Handles incoming client connections.
  ```python
  def receive_connections():
      print("Server is running and listening...")
      while True:
          client, address = server.accept()
          print(f"Connected with {str(address)}")
  ```

### **Client (`mian.py`)**

#### **Configuration**
```python
HOST = server.HOST  # Server's IP
PORT = 9090         # Port to connect to
```
The client connects to the server using the specified host IP and port.

#### **Key Functions**
- **Receive Messages**: Listens for messages from the server.
  ```python
  def receive_messages():
      while True:
          try:
              message = client.recv(1024).decode('utf-8')
              if message == 'NICKNAME':
                  client.send(nickname.encode('utf-8'))
              else:
                  print(message)
          except:
              print("An error occurred!")
              client.close()
              break
  ```
- **Send Messages**: Sends messages to the server.
  ```python
  def send_messages():
      while True:
          message = f'{nickname}: {input("")}'
          client.send(message.encode('utf-8'))
  ```

---

## ⚡ Example Usage
1. Start the server:
   ```bash
   python server.py
   ```
   Output:
   ```plaintext
   Server is running and listening...
   Connected with ('127.0.0.1', 54321)
   Nickname of the client is Batman
   ```

2. Start the client:
   ```bash
   python mian.py
   ```
   Output:
   ```plaintext
   Choose your nickname: Batman
   Connected to the server!
   ```
3. Chat with multiple clients:
   ```plaintext
   Batman: Hello, everyone!
   Superman: Hey Batman!
   ```

---

## 📝 Improvements
- Add authentication for secure connections.
- Implement message encryption.
- Improve user interface using a graphical library such as `tkinter`.
- Handle more error scenarios gracefully.

---

## 🏗️ Project Architecture
| Component | Description |
|-----------|-------------|
| Server    | Handles multiple client connections and message broadcasting |
| Client    | Connects to the server and sends/receives messages |

---

## 💭 Quotes
> \"Good communication is as stimulating as black coffee and just as hard to sleep after.\" — Anne Morrow Lindbergh

---

## 📚 Resources
- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [Threading Documentation](https://docs.python.org/3/library/threading.html)

---

## 🖊️ Author
**Muhammad Ahmad Nadeem**

Feel free to reach out if you have any questions or suggestions!

---

## 🌟 Acknowledgments
Special thanks to everyone who contributes to making open-source projects awesome!
