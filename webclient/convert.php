<?php

header("Access-Control-Allow-Origin: *");
function send_post($url, $post_data) {
 
  $options = array(
    'http' => array(
      'method' => 'POST',
      'header' => 'Access-Control-Allow-Origin: *',
      'content' => $post_data,
      'timeout' => 15 * 60 // 超时时间（单位:s）
    )
  );
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
 
  return $result;
}
 
//使用方法
$post_data = $_POST;
send_post('http://47.94.148.72:1262/trans', $post_data);