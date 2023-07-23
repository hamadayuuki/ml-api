// MARK: - メッセージを作成
function sayUser(message) {
  // 右側にチャットボックスを作成
  const chatbox =
    '<li><div class="balloon balloon-r">' +
      '<p class="say say-r">' +
        message +
      '</p>' +
    '</div></li>';
  $('#chat-area').append(chatbox);
  // メッセージ最下部までスクロール
  $(window).scrollTop($('#chat-area')[0].scrollHeight);
}

function sayOperator(message) {
  // メッセージを表示するため、htmlにメッセージ一覧を注入
  const chatbox =
    '<li><div class="balloon">' +
      '<img class="img-circle" src="{{ url_for("static", filename="images/operator.png") }}" alt="operator" />' +
      '<p class="say">' +
        message +
      '</p>' +
    '</div></li>';
  $('#chat-area').append(chatbox);

  $(window).scrollTop($('#chat-area')[0].scrollHeight);
}


// MARK: - Read
function read() {
  $('#chat-area').empty();   // メッセージ一覧初期化

  fetch('/v1/read', {
    method: 'GET',
  })
  .then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    return res.json();
  })
  .then((v) => {
    v.forEach((message) => {
      if (message.name === "me") {
        sayUser(message.message);
      } else {
        sayOperator(message.message);
      }
    })
    .catch(e => {
      console.log('There was a problem with your fetch operation: ' + e.message);
    });
  });
}

window.onload = read;


// MARK: - Update
function update() {
  $('#chat-area').empty();

  const name = "me";
  const message = $('#msg-send').val();   // 入力した文字列

  fetch('/v1/update?' + 'name=' + name + '&message=' + message, {
    method: 'GET',
  })
  .then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    return res.json();
  })
  .then((v) => {
    v.forEach((message) => {
      if (message.name === "me") {
        sayUser(message.message);
      } else {
        sayOperator(message.message);
      }
    })
    .catch(e => {
      console.log('There was a problem with your fetch operation: ' + e.message);
    });
  });
}


// MARK: - Delete
// 1 : htmlに「メッセージ削除ボタン」を追加
// 2 : javascriptに "v1/delete" へリクエストする処理を書く
//         - "v1/read, update" を参考にする
// extra : メッセージを指定した削除を可能とする
