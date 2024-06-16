<%@page import="board.bean.BoardDTO"%>
<%@page import="board.dao.BoardDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>글수정</title>
<script type="text/javascript" src="../script/boardScript.js">
</script>
</head>
<body>
<form action="" method="post" name="boardModifyForm">
	<input type="hidden" name="seq" value="${seq }">
	<input type="hidden" name="pg" value="${pg }">
	<table border="1">
		<tr>
			<th width="50">제목</th>
			<td>
				<input type="text" name="subject" id="subject" size="59"
					value="${boardDTO.subject}">
			</td>
		</tr>
		<tr>
			<th>내용</th>
			<td>
				<textarea name="content" id="content" rows="15" cols="45">${boardDTO.content}</textarea>
			</td>
		</tr>
		<tr>			
			<td colspan="2" align="center">
				<input type="button" value="글수정" onclick="checkBoardModify()">
				<input type="reset" value="다시 작성">
			</td>
		</tr>
	</table>
</form>	
<a href="../main/index">메인 화면</a>
</body>
</html>













