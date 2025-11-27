---
layout: default
title: Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models
---

# Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models
**arXiv**：[2511.21663v1](https://arxiv.org/abs/2511.21663) · [PDF](https://arxiv.org/pdf/2511.21663.pdf)  
**作者**：Naifu Zhang, Wei Tao, Xi Xiao, Qianpu Sun, Yuxin Zheng, Wentao Mo, Peiqiang Wang, Nan Zhang  

**一句话要点**：提出ADVLA框架以高效攻击视觉-语言-动作模型，实现低幅度稀疏扰动

**关键词**：对抗攻击, 视觉-语言-动作模型, 稀疏扰动, 注意力引导, 特征空间攻击

## 3 点简述
- 现有对抗攻击方法需高成本端到端训练且扰动明显
- ADVLA在视觉编码器投影特征上施加扰动，结合注意力引导实现稀疏性
- 实验显示在低幅度约束下，修改少于10%补丁，攻击成功率近100%

## 摘要（原文）

> In recent years, Vision-Language-Action (VLA) models in embodied intelligence have developed rapidly. However, existing adversarial attack methods require costly end-to-end training and often generate noticeable perturbation patches. To address these limitations, we propose ADVLA, a framework that directly applies adversarial perturbations on features projected from the visual encoder into the textual feature space. ADVLA efficiently disrupts downstream action predictions under low-amplitude constraints, and attention guidance allows the perturbations to be both focused and sparse. We introduce three strategies that enhance sensitivity, enforce sparsity, and concentrate perturbations. Experiments demonstrate that under an $L_{\infty}=4/255$ constraint, ADVLA combined with Top-K masking modifies less than 10% of the patches while achieving an attack success rate of nearly 100%. The perturbations are concentrated on critical regions, remain almost imperceptible in the overall image, and a single-step iteration takes only about 0.06 seconds, significantly outperforming conventional patch-based attacks. In summary, ADVLA effectively weakens downstream action predictions of VLA models under low-amplitude and locally sparse conditions, avoiding the high training costs and conspicuous perturbations of traditional patch attacks, and demonstrates unique effectiveness and practical value for attacking VLA feature spaces.

