const baseURL = "https://ml-api-nn8r.onrender.com";

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
      //'<img class="img-circle" src="{{ url_for("static", filename="images/operator.png") }}" alt="operator" />' +
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

  fetch(baseURL + '/v1/read', {
    method: 'GET',
  })
  .then((res) => res.json())
  .then((v) => {
    v.forEach((message) => {
      if (message.name === "me") {
        sayUser(message.message);
      } else {
        sayOperator(message.message);
      }
    });
  });
}

window.onload = read;


// MARK: - Update
function update() {
  $('#chat-area').empty();

  fetch(baseURL + '/v1/update', {
    method: 'GET',
  })
  .then((res) => res.json())
  .then((v) => {
    v.forEach((message) => {
      if (message.name === "me") {
        sayUser(message.message);
      } else {
        sayOperator(message.message);
      }
    });
  });
}

$("#msg-send").keydown(function (e) {
  // 「Shift」+「Enter」を押したか
  if (e.keyCode === 13 && e.shiftKey) {
    e.preventDefault();  // Shift+Enterでのデフォルトの動作（改行）を防ぐ
    update();
  }
});


// MARK: - Delete
// 1 : htmlに「メッセージ削除ボタン」を追加
// 2 : javascriptに "v1/delete" へリクエストする処理を書く
//         - "v1/read, update" を参考にする
// extra : メッセージを指定した削除を可能とする
