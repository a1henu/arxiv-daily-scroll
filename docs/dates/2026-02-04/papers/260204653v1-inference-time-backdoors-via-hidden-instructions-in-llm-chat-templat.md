---
layout: default
title: Inference-Time Backdoors via Hidden Instructions in LLM Chat Templates
---

# Inference-Time Backdoors via Hidden Instructions in LLM Chat Templates
**arXiv**：[2602.04653v1](https://arxiv.org/abs/2602.04653) · [PDF](https://arxiv.org/pdf/2602.04653.pdf)  
**作者**：Ariel Fogel, Omer Hofman, Eilon Cohen, Roman Vainshtein  

**一句话要点**：提出利用聊天模板植入推理时后门攻击，无需修改模型权重或控制基础设施。

**关键词**：聊天模板攻击, 推理时后门, 语言模型安全, 供应链安全, 自动化扫描规避

## 3 点简述
- 核心问题：开放权重语言模型在推理时面临聊天模板作为新攻击面的安全威胁。
- 方法要点：通过恶意修改聊天模板植入后门，在特定触发条件下激活隐藏行为。
- 实验或效果：在触发条件下，事实准确性平均从90%降至15%，攻击者控制URL发射成功率超80%。

## 摘要（原文）

> Open-weight language models are increasingly used in production settings, raising new security challenges. One prominent threat in this context is backdoor attacks, in which adversaries embed hidden behaviors in language models that activate under specific conditions. Previous work has assumed that adversaries have access to training pipelines or deployment infrastructure. We propose a novel attack surface requiring neither, which utilizes the chat template. Chat templates are executable Jinja2 programs invoked at every inference call, occupying a privileged position between user input and model processing. We show that an adversary who distributes a model with a maliciously modified template can implant an inference-time backdoor without modifying model weights, poisoning training data, or controlling runtime infrastructure. We evaluated this attack vector by constructing template backdoors targeting two objectives: degrading factual accuracy and inducing emission of attacker-controlled URLs, and applied them across eighteen models spanning seven families and four inference engines. Under triggered conditions, factual accuracy drops from 90% to 15% on average while attacker-controlled URLs are emitted with success rates exceeding 80%; benign inputs show no measurable degradation. Backdoors generalize across inference runtimes and evade all automated security scans applied by the largest open-weight distribution platform. These results establish chat templates as a reliable and currently undefended attack surface in the LLM supply chain.

