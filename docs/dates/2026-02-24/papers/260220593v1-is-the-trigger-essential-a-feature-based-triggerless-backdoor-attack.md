---
layout: default
title: Is the Trigger Essential? A Feature-Based Triggerless Backdoor Attack in Vertical Federated Learning
---

# Is the Trigger Essential? A Feature-Based Triggerless Backdoor Attack in Vertical Federated Learning
**arXiv**：[2602.20593v1](https://arxiv.org/abs/2602.20593) · [PDF](https://arxiv.org/pdf/2602.20593.pdf)  
**作者**：Yige Liu, Yiwei Lou, Che Wang, Yongzhi Cao, Hanpin Wang  

**一句话要点**：提出特征式无触发器后门攻击以揭示垂直联邦学习安全威胁

**关键词**：垂直联邦学习, 后门攻击, 无触发器攻击, 特征毒化, 安全威胁, 鲁棒性

## 3 点简述
- 核心问题：现有后门攻击依赖触发器，在垂直联邦学习中可能非必需，存在未知攻击路径。
- 方法要点：基于特征设计无触发器攻击，包含标签推断、毒化生成与后门执行模块，假设攻击者诚实但好奇。
- 实验效果：在五个基准数据集上优于基线攻击2至50倍，对主任务影响小，且对防御策略鲁棒性强。

## 摘要（原文）

> As a distributed collaborative machine learning paradigm, vertical federated learning (VFL) allows multiple passive parties with distinct features and one active party with labels to collaboratively train a model. Although it is known for the privacy-preserving capabilities, VFL still faces significant privacy and security threats from backdoor attacks. Existing backdoor attacks typically involve an attacker implanting a trigger into the model during the training phase and executing the attack by adding the trigger to the samples during the inference phase. However, in this paper, we find that triggers are not essential for backdoor attacks in VFL. In light of this, we disclose a new backdoor attack pathway in VFL by introducing a feature-based triggerless backdoor attack. This attack operates under a more stringent security assumption, where the attacker is honest-but-curious rather than malicious during the training phase. It comprises three modules: label inference for the targeted backdoor attack, poison generation with amplification and perturbation mechanisms, and backdoor execution to implement the attack. Extensive experiments on five benchmark datasets demonstrate that our attack outperforms three baseline backdoor attacks by 2 to 50 times while minimally impacting the main task. Even in VFL scenarios with 32 passive parties and only one set of auxiliary data, our attack maintains high performance. Moreover, when confronted with distinct defense strategies, our attack remains largely unaffected and exhibits strong robustness. We hope that the disclosure of this triggerless backdoor attack pathway will encourage the community to revisit security threats in VFL scenarios and inspire researchers to develop more robust and practical defense strategies.

