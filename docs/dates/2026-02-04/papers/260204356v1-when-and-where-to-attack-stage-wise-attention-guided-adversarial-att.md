---
layout: default
title: When and Where to Attack? Stage-wise Attention-Guided Adversarial Attack on Large Vision Language Models
---

# When and Where to Attack? Stage-wise Attention-Guided Adversarial Attack on Large Vision Language Models
**arXiv**：[2602.04356v1](https://arxiv.org/abs/2602.04356) · [PDF](https://arxiv.org/pdf/2602.04356.pdf)  
**作者**：Jaehyun Kwak, Nam Cao, Boryeong Cho, Segyu Lee, Sumyeong Ahn, Se-Young Yun  

**一句话要点**：提出阶段式注意力引导攻击（SAGA），以高效利用扰动预算攻击大型视觉语言模型。

**关键词**：对抗攻击, 大型视觉语言模型, 注意力机制, 扰动优化, 多模态安全

## 3 点简述
- 核心问题：现有对抗攻击随机裁剪图像，效率低且未充分利用扰动预算。
- 方法要点：基于注意力分数与对抗损失敏感性正相关，逐步集中扰动于高注意力区域。
- 实验或效果：在十个LVLM上实现最先进的攻击成功率，生成难以察觉的对抗样本。

## 摘要（原文）

> Adversarial attacks against Large Vision-Language Models (LVLMs) are crucial for exposing safety vulnerabilities in modern multimodal systems. Recent attacks based on input transformations, such as random cropping, suggest that spatially localized perturbations can be more effective than global image manipulation. However, randomly cropping the entire image is inherently stochastic and fails to use the limited per-pixel perturbation budget efficiently. We make two key observations: (i) regional attention scores are positively correlated with adversarial loss sensitivity, and (ii) attacking high-attention regions induces a structured redistribution of attention toward subsequent salient regions. Based on these findings, we propose Stage-wise Attention-Guided Attack (SAGA), an attention-guided framework that progressively concentrates perturbations on high-attention regions. SAGA enables more efficient use of constrained perturbation budgets, producing highly imperceptible adversarial examples while consistently achieving state-of-the-art attack success rates across ten LVLMs. The source code is available at https://github.com/jackwaky/SAGA.

