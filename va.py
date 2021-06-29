var exec = require('child_process').exec
function CERT_createKey(CN,keylen,callback){
        exec('openssl genrsa -out '+CN+'.key '+keylen, function(error, stdout, stderr) {
            if(error !== null) {
                console.log("Create Cert Key : " + error);
                callback({fail:true,error:error});
            } else {
                callback({fail:false,error:"none"});
            }
        });
    }

function CERT_csr(CN,callback){
        exec('openssl req -new -key '+CN+'.key -nodes -subj "/C=KR/O=noweek, Inc./OU=www.securekim.com/OU=(c) 2018 noweek, Inc./CN='
    +CN+'" -out '+CN+'.csr', function(error, stdout, stderr) {
            if(error !== null) {
                console.log("Create CSR : " + error);
                callback({fail:true,error:error});
            } else {
                callback({fail:false,error:"none"});
            }
        }); }

