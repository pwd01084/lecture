var net = require('net');
function getConnection(connName) {
    
    var client = net.connect({ port: 8107, host: '172.22.129.226' }, function () {
        console.log(connName)
        this.setTimeout(500);//ms
        this.setEncoding('utf8');
        this.on('data', function (data) {
            console.log(data)
            this.end();
        });
        this.on('end', function () {
        });
        this.on('error', function (err) {
            console.log(err)
        });
        this.on('timeout', function () {
        });
        this.on('close', function () {
        });
    });
    return client;
}

function writeData(socket, data) {
    var success = !socket.write(data);
    if (!success) {
        (function (socket, data) {
            socket.once('drain', function () {
                writeData(socket, data);
            });
        })(socket, data);
    }
}
var Alice = getConnection("Alice's Connection");
var Bob = getConnection("Bob's Connection");
writeData(Alice, "Alice|Hi, Server");
writeData(Bob, "Bob|Hello, Server");