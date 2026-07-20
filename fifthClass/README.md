> Instalar PHP

> Linux
```
sudo apt install php8.3-cli
```

> Windows
```
1. Baixar o PHPAcesse o site oficial: windows.php.net.Baixe a versão estável mais recente (ex: PHP 8.3 ou superior).Escolha a opção VS16 x64 Thread Safe (arquivo Zip).
2. Extrair os arquivosCrie uma pasta chamada php diretamente no seu disco local, por exemplo: C:\php.Extraia todo o conteúdo do arquivo Zip baixado dentro dessa pasta.3. Configurar as Variáveis de AmbientePara o Windows reconhecer o comando php no terminal, faça o seguinte:Pressione a tecla Win, digite "variáveis de ambiente" e clique em "Editar as variáveis de ambiente do sistema".Clique no botão Variáveis de Ambiente... (na parte inferior).Na lista "Variáveis do Sistema", procure pela variável Path e dê um duplo clique.Clique em Novo e adicione o caminho da sua pasta: C:\php.Clique em OK em todas as janelas abertas para salvar.4. Testar a instalaçãoAbra o Prompt de Comando (CMD) ou o PowerShell.Digite o comando: php -v.O terminal exibirá a versão exata do PHP instalada.
```
> Executar
```
php -S localhost:8000
```


