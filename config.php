<?php

    $dbHost = 'gate.jelastic.saveincloud.net';
    $dbUsername = '157812-25094';
    $dbPassword = '';
    $dbName = 'formulario';

    $conexao = new mysqli($dbHost,$dbUsername,$dbPassword,$dbName);

    if($conexao->connect_errno)
    {
        echo "Erro";
    }
    else
    {
        echo "Conexão efetuada com sucesso"
    }

?>