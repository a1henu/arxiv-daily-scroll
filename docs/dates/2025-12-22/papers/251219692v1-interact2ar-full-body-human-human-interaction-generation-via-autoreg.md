---
layout: default
title: Interact2Ar: Full-Body Human-Human Interaction Generation via Autoregressive Diffusion Models
---

# Interact2Ar: Full-Body Human-Human Interaction Generation via Autoregressive Diffusion Models
**arXiv**：[2512.19692v1](https://arxiv.org/abs/2512.19692) · [PDF](https://arxiv.org/pdf/2512.19692.pdf)  
**作者**：Pablo Ruiz-Ponce, Sergio Escalera, José García-Rodríguez, Jiankang Deng, Rolandos Alexandros Potamias  

**一句话要点**：提出Interact2Ar，首个端到端文本条件自回归扩散模型，用于生成全身人-人交互动作。

**关键词**：人-人交互生成, 自回归扩散模型, 全身动作合成, 手部运动学, 文本条件生成, 交互评估指标

## 3 点简述
- 核心问题：现有方法忽略手部动作，且扩散模型同时生成整个序列，难以捕捉交互的反应性和适应性。
- 方法要点：通过并行分支整合手部运动学，结合自回归管道和新颖记忆技术，利用大上下文窗口适应交互变异性。
- 实验或效果：引入专门评估指标，定量和定性实验显示在全身交互生成上达到先进性能，支持下游应用如实时适应。

## 摘要（原文）

> Generating realistic human-human interactions is a challenging task that requires not only high-quality individual body and hand motions, but also coherent coordination among all interactants. Due to limitations in available data and increased learning complexity, previous methods tend to ignore hand motions, limiting the realism and expressivity of the interactions. Additionally, current diffusion-based approaches generate entire motion sequences simultaneously, limiting their ability to capture the reactive and adaptive nature of human interactions. To address these limitations, we introduce Interact2Ar, the first end-to-end text-conditioned autoregressive diffusion model for generating full-body, human-human interactions. Interact2Ar incorporates detailed hand kinematics through dedicated parallel branches, enabling high-fidelity full-body generation. Furthermore, we introduce an autoregressive pipeline coupled with a novel memory technique that facilitates adaptation to the inherent variability of human interactions using efficient large context windows. The adaptability of our model enables a series of downstream applications, including temporal motion composition, real-time adaptation to disturbances, and extension beyond dyadic to multi-person scenarios. To validate the generated motions, we introduce a set of robust evaluators and extended metrics designed specifically for assessing full-body interactions. Through quantitative and qualitative experiments, we demonstrate the state-of-the-art performance of Interact2Ar.

