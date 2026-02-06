## Documentação Python 
## O que há de novo no Python 3.14

Este artigo explica os novos recursos do Python 3.14, em comparação com o 3.13. Python 3.14 foi lançado em 7 de outubro de 2025. Veja [changelog](https://docs.python.org/pt-br/3/whatsnew/3.14.html) para uma lista completa de mudanças.

## Resumo – Destaques da versão

Python 3.14 é a versão estável mais recente da linguagem de programação Python, com uma mistura de alterações na linguagem, na implementação e na biblioteca padrão. As maiores mudanças incluem: [literais de string template, avaliação adiada de anotações](https://docs.python.org/pt-br/3/whatsnew/3.14.html) e suporte para subinterpretadores na biblioteca padrão.

As mudanças na biblioteca incluem recursos significativamente melhorados para [introspecção no asyncio, suporte para Zstandard](https://docs.python.org/pt-br/3/whatsnew/3.14.html) por meio de um novo módulo [compression.zstd](https://docs.python.org/pt-br/3/whatsnew/3.14.html), destaque de sintaxe no REPL, bem como as descontinuações e remoções habituais e melhorias na facilidade de uso e correção.

Este artigo não tenta fornecer uma especificação completa de todos os novos recursos, mas fornece uma visão geral conveniente. Para detalhes completos, consulte a documentação, como [Referência da Biblioteca](https://docs.python.org/pt-br/3/whatsnew/3.14.html) e [Referência da Linguagem](https://docs.python.org/pt-br/3/whatsnew/3.14.html). Para entender a implementação completa e a justificativa do design para uma mudança, consulte a PEP para um novo recurso específico; mas observe que as PEPs geralmente não são mantidas atualizadas depois que um recurso é totalmente implementado. Veja [Portando para o Python 3.14](https://docs.python.org/pt-br/3/whatsnew/3.14.html) para orientação sobre atualização a partir de versões anteriores do Python.

Melhorias no interpretador:

- [PEP 649 e PEP 749: avaliação adiada de anotações](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [PEP 734: múltiplos interpretadores na biblioteca padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [PEP 750: strings template](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [PEP 758: permitir expressões except e except* sem parênteses](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [PEP 765: fluxo de controle em blocos finally](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [PEP 768: interface segura para depurador externo para CPython](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Um novo tipo de interpretador](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Melhorias no modo com threads livres](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Mensagens de erro melhoradas](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Coleta de lixo incremental](https://docs.python.org/pt-br/3/whatsnew/3.14.html)

Melhorias significativas na biblioteca padrão:

- [PEP 784: suporte ao Zstandard na biblioteca padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Capacidades de introspecção assíncrona](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Controle de avisos seguros simultâneos](https://docs.python.org/pt-br/3/whatsnew/3.14.html)
- [Realce de sintaxe no console interativo padrão](https://docs.python.org/pt-br/3/whatsnew/3.14.html) e saída colorida em várias interfaces de linha de comando (CLIs) de módulos da biblioteca padrão
