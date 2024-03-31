DESAFIO TÉCNICO (ESTÁGIO/JR) – QUALITY ASSURANCE ENGINEER
Proposta: Criar e automatizar possíveis cenários de teste de um projeto web baseando na página de login do site “Automation Practice”.

Cenário 1: Verificar se o login com informações válidas está funcionando corretamente.
  - Dado que o usuário esteja na página de login
  - Quando o usuário inserir informações válidas de login
  - Então o usuário deve ser redirecionado para a página da sua conta

Cenário 2: Verificar login com email não cadastrado.
  - Dado que o usuário esteja na página de login
  - Quando o usuário inserir um e-mail não cadastrado
  - Então o usuário deve receber uma mensagem de erro contendo a informação de email inválido.

Cenário 3: Verificar login com senha incorreta
  - Dado que o usuário esteja na página de login
  - Quando o usuário inserir uma senha inválida
  - Então o usuário deve receber uma mensagem de senha inválida.

Outras sugestões de cenário:
Cenário 4: Verificar se o e-mail digitado para criar conta é de fato um email com domínio válido (gmail, hotmail, outlook...).
Cenário 5: Verificar se há mensagem de erro para campos obrigatórios vazios (email ou senha).
