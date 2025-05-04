
# Projeto-CRUD-Python
CRUD em Python

#Branch

1. main
Propósito: É a ramificação principal e estável.

Regra: Só deve conter código pronto para produção.


2. develop
Propósito: Onde o desenvolvimento contínuo acontece.

Regra: Funciona como uma versão instável, onde são mescladas as features em andamento antes de irem para a main.


3. feature/nome-da-funcionalidade
Propósito: Usado para desenvolver novas funcionalidades ou melhorias.

Exemplo: feature/login, feature/chat-integracao

Fluxo comum: Começa a partir de develop e depois é mesclado de volta quando finalizado.


4. bugfix/nome-do-bug
Propósito: Corrigir erros identificados em ambiente de desenvolvimento.

Exemplo: bugfix/erro-login, bugfix/filtro-produtos


5. hotfix/nome-do-hotfix
Propósito: Corrigir erros críticos diretamente na produção.

Fluxo: Começa a partir de main e deve ser mesclado de volta em main e develop.

Exemplo: hotfix/seguranca-api

6. release/nome-da-versao
Propósito: Preparar uma nova versão para produção.

Fluxo: Criada a partir de develop, testada e depois mesclada em main e develop.

Exemplo: release/v1.0.0 (

1 - MAJOR (versão principal)	Muda quando há grandes mudanças que quebram a compatibilidade com versões anteriores. Ex: o sistema muda completamente ou APIs antigas param de funcionar.

0 - MINOR (versão secundária)	Muda quando há funcionalidades novas adicionadas de forma compatível com o que já existia. Ex: você adiciona um novo recurso, mas nada antigo quebra.

0 - PATCH (correções)	Muda quando há correções de bugs ou pequenas melhorias, sem alterar funcionalidades nem quebrar nada.
    
)
