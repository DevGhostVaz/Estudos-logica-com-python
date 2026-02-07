## Documentação Python 
## O que há de novo no Python 3.14

Este artigo explica os novos recursos do Python 3.14, em comparação com o 3.13. Python 3.14 foi lançado em 7 de outubro de 2025. Veja [changelog](https://docs.python.org/pt-br/3/whatsnew/changelog.html#changelog) para uma lista completa de mudanças.

## Resumo – Destaques da versão

Python 3.14 é a versão estável mais recente da linguagem de programação Python, com uma mistura de alterações na linguagem, na implementação e na biblioteca padrão. As maiores mudanças incluem: [literais de string template, avaliação adiada de anotações](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-template-string-literals) e suporte para subinterpretadores na biblioteca padrão.

As mudanças na biblioteca incluem recursos significativamente melhorados para [introspecção no asyncio, suporte para Zstandard](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-asyncio-introspection) por meio de um novo módulo [compression.zstd](https://docs.python.org/pt-br/3/library/compression.zstd.html#module-compression.zstd), destaque de sintaxe no REPL, bem como as descontinuações e remoções habituais e melhorias na facilidade de uso e correção.

Este artigo não tenta fornecer uma especificação completa de todos os novos recursos, mas fornece uma visão geral conveniente. Para detalhes completos, consulte a documentação, como [Referência da Biblioteca](https://docs.python.org/pt-br/3/library/index.html#library-index) e [Referência da Linguagem](https://docs.python.org/pt-br/3/reference/index.html#reference-index). Para entender a implementação completa e a justificativa do design para uma mudança, consulte a PEP para um novo recurso específico; mas observe que as PEPs geralmente não são mantidas atualizadas depois que um recurso é totalmente implementado. Veja [Portando para o Python 3.14](https://docs.python.org/pt-br/3/whatsnew/3.14.html#porting-to-python-3-14) para orientação sobre atualização a partir de versões anteriores do Python.

Melhorias no interpretador:

- [PEP 649 e PEP 749: avaliação adiada de anotações](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-deferred-annotations)
- [PEP 734: múltiplos interpretadores na biblioteca padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-multiple-interpreters)
- [PEP 750: strings template](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-template-string-literals)
- [PEP 758: permitir expressões except e except* sem parênteses](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-bracketless-except)
- [PEP 765: fluxo de controle em blocos finally](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-finally-syntaxwarning)
- [PEP 768: interface segura para depurador externo para CPython](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-remote-debugging)
- [Um novo tipo de interpretador](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-tail-call-interpreter)
- [Melhorias no modo com threads livres](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-free-threaded-cpython)
- [Mensagens de erro melhoradas](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-improved-error-messages)
- [Coleta de lixo incremental](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-incremental-gc)

Melhorias significativas na biblioteca padrão:

- [PEP 784: suporte ao Zstandard na biblioteca padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-zstandard)
- [Capacidades de introspecção assíncrona](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-asyncio-introspection)
- [Controle de avisos seguros simultâneos](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-concurrent-warnings-control)
- [Realce de sintaxe no console interativo padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-pyrepl-highlighting) e saída colorida em várias interfaces de linha de comando (CLIs) de módulos da biblioteca padrão

Melhorias na API C:

- [PEP 741: API C de configuração do Python](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-capi-config)

Suporte à plataforma:

- [PEP 776](https://peps.python.org/pep-0776/): Emscripten agora é uma [plataforma oficialmente com suporte](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-build-changes), no [nível 3](https://peps.python.org/pep-0011/#tier-3).

Alterações na versão:

- [PEP 779](https://peps.python.org/pep-0779/): [Python com threads livres é oficialmente suportado](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-free-threaded-now-supported)
- [PEP 761](https://peps.python.org/pep-0761/): [Assinaturas PGP foram descontinuadas de lançamentos oficiais](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-no-more-pgp)
- [Versões binárias de Windows e macOS agora oferecem suporte ao compilador experimental just-in-time](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-jit-compiler)
- [Versões binárias para Android são agora fornecidas](https://docs.python.org/pt-br/3/whatsnew/3.14.html#whatsnew314-jit-compiler)

## Novas funcionalidades
