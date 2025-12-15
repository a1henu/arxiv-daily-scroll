---
layout: default
title: Smudged Fingerprints: A Systematic Evaluation of the Robustness of AI Image Fingerprints
---

# Smudged Fingerprints: A Systematic Evaluation of the Robustness of AI Image Fingerprints
**arXiv**：[2512.11771v1](https://arxiv.org/abs/2512.11771) · [PDF](https://arxiv.org/pdf/2512.11771.pdf)  
**作者**：Kai Yao, Marc Juarez  

**一句话要点**：系统评估AI图像指纹的鲁棒性，揭示其在对抗攻击下的脆弱性

**关键词**：AI图像指纹, 对抗攻击, 鲁棒性评估, 模型归因, 安全威胁模型

## 3 点简述
- 核心问题：AI图像指纹检测技术在对抗条件下的鲁棒性未知，威胁模型包括白盒和黑盒访问。
- 方法要点：提出五种攻击策略，评估14种指纹方法在RGB、频率和特征域的鲁棒性。
- 实验或效果：移除攻击在白盒下成功率超80%，黑盒下超50%；指纹伪造成功率因目标模型而异，存在准确性与鲁棒性权衡。

## 摘要（原文）

> Model fingerprint detection techniques have emerged as a promising approach for attributing AI-generated images to their source models, but their robustness under adversarial conditions remains largely unexplored. We present the first systematic security evaluation of these techniques, formalizing threat models that encompass both white- and black-box access and two attack goals: fingerprint removal, which erases identifying traces to evade attribution, and fingerprint forgery, which seeks to cause misattribution to a target model. We implement five attack strategies and evaluate 14 representative fingerprinting methods across RGB, frequency, and learned-feature domains on 12 state-of-the-art image generators. Our experiments reveal a pronounced gap between clean and adversarial performance. Removal attacks are highly effective, often achieving success rates above 80% in white-box settings and over 50% under constrained black-box access. While forgery is more challenging than removal, its success significantly varies across targeted models. We also identify a utility-robustness trade-off: methods with the highest attribution accuracy are often vulnerable to attacks. Although some techniques exhibit robustness in specific settings, none achieves high robustness and accuracy across all evaluated threat models. These findings highlight the need for techniques balancing robustness and accuracy, and identify the most promising approaches for advancing this goal.

