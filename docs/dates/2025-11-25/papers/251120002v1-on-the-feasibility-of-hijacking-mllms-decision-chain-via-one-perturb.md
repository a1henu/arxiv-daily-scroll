---
layout: default
title: On the Feasibility of Hijacking MLLMs' Decision Chain via One Perturbation
---

# On the Feasibility of Hijacking MLLMs' Decision Chain via One Perturbation
**arXiv**：[2511.20002v1](https://arxiv.org/abs/2511.20002) · [PDF](https://arxiv.org/pdf/2511.20002.pdf)  
**作者**：Changyue Li, Jiaying Li, Youliang Yuan, Jiaming He, Zhicong Huang, Pinjia He  

**一句话要点**：提出语义感知通用扰动以劫持多模态大语言模型决策链

**关键词**：对抗攻击, 决策链劫持, 语义感知扰动, 多模态大语言模型, 安全风险

## 3 点简述
- 核心问题：传统对抗攻击仅操纵单一决策，而真实模型决策链中的级联错误可能导致严重风险。
- 方法要点：引入语义感知通用扰动，通过归一化空间搜索和语义分离策略实现多目标操控。
- 实验或效果：在三个多模态大语言模型上测试，使用对抗帧控制五个目标时攻击成功率高达70%。

## 摘要（原文）

> Conventional adversarial attacks focus on manipulating a single decision of neural networks. However, real-world models often operate in a sequence of decisions, where an isolated mistake can be easily corrected, but cascading errors can lead to severe risks.
>   This paper reveals a novel threat: a single perturbation can hijack the whole decision chain. We demonstrate the feasibility of manipulating a model's outputs toward multiple, predefined outcomes, such as simultaneously misclassifying "non-motorized lane" signs as "motorized lane" and "pedestrian" as "plastic bag".
>   To expose this threat, we introduce Semantic-Aware Universal Perturbations (SAUPs), which induce varied outcomes based on the semantics of the inputs. We overcome optimization challenges by developing an effective algorithm, which searches for perturbations in normalized space with a semantic separation strategy. To evaluate the practical threat of SAUPs, we present RIST, a new real-world image dataset with fine-grained semantic annotations. Extensive experiments on three multimodal large language models demonstrate their vulnerability, achieving a 70% attack success rate when controlling five distinct targets using just an adversarial frame.

