---
layout: default
title: Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search
---

# Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search
**arXiv**：[2602.22983v1](https://arxiv.org/abs/2602.22983) · [PDF](https://arxiv.org/pdf/2602.22983.pdf)  
**作者**：Xun Huang, Simeng Qin, Xiaoshuang Jia, Ranjie Duan, Huanqian Yan, Zhitao Zeng, Fei Yang, Yang Liu, Xiaojun Jia  

**一句话要点**：提出CC-BOS框架，利用古典中文和果蝇优化算法自动化生成对抗提示以增强黑盒越狱攻击效果。

**关键词**：大语言模型安全, 越狱攻击, 古典中文对抗提示, 果蝇优化算法, 黑盒攻击

## 3 点简述
- 研究古典中文在LLM越狱攻击中的作用，因其简洁隐晦可部分绕过安全约束。
- 基于多维果蝇优化设计CC-BOS框架，自动生成古典中文对抗提示，覆盖八个策略维度。
- 实验表明CC-BOS在黑盒设置下优于现有越狱攻击方法，并设计翻译模块提升可读性。

## 摘要（原文）

> As Large Language Models (LLMs) are increasingly used, their security risks have drawn increasing attention. Existing research reveals that LLMs are highly susceptible to jailbreak attacks, with effectiveness varying across language contexts. This paper investigates the role of classical Chinese in jailbreak attacks. Owing to its conciseness and obscurity, classical Chinese can partially bypass existing safety constraints, exposing notable vulnerabilities in LLMs. Based on this observation, this paper proposes a framework, CC-BOS, for the automatic generation of classical Chinese adversarial prompts based on multi-dimensional fruit fly optimization, facilitating efficient and automated jailbreak attacks in black-box settings. Prompts are encoded into eight policy dimensions-covering role, behavior, mechanism, metaphor, expression, knowledge, trigger pattern and context; and iteratively refined via smell search, visual search, and cauchy mutation. This design enables efficient exploration of the search space, thereby enhancing the effectiveness of black-box jailbreak attacks. To enhance readability and evaluation accuracy, we further design a classical Chinese to English translation module. Extensive experiments demonstrate that effectiveness of the proposed CC-BOS, consistently outperforming state-of-the-art jailbreak attack methods.

