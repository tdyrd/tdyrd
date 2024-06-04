//注册时判断用户名是否存在

public static boolean UserExists(String username) {

//可以建立一个连接池保存一定数量的连接，当有对象需要数据库连接时，直接将这个连接返回给该对象，

ConnectionPool pool = ConnectionPool.getInstance();

Connection connection = pool.getConnection();

PreparedStatement ps = null;

ResultSet rs = null;

String qr = "SELECT username FROM User "+ “WHERE username = ?”;

try {

ps = connection.prepareStatement(qr);

ps.setString(1, username);

rs = ps.executeQuery();

return rs.next();

} catch (SQLException e) {

System.out.println(e);

return false;

} finally {

DBUtil.closeResultSet(rs);

DBUtil.closePreparedStatement(ps);

pool.freeConnection(connection);

}

}

//将注册用户信息保存至数据库

public static int insert(User user) {

ConnectionPool pool = ConnectionPool.getInstance();

Connection connection = pool.getConnection();

PreparedStatement ps = null;

String qr = “INSERT INTO User (username, password)”+“VALUES (?, ?)”;

try {

ps = connection.prepareStatement(qr);

ps.setString(1, user.getusername());

ps.setString(2, user.getpassword());

return ps.executeUpdate();

} catch (SQLException e) {

System.out.println(e);

return 0;

} finally {

DBUtil.closePreparedStatement(ps);

pool.freeConnection(connection);

}

}

