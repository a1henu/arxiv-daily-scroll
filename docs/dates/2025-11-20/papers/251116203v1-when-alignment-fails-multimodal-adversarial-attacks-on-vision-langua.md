---
layout: default
title: When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models
---

# When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models
**arXiv**：[2511.16203v1](https://arxiv.org/abs/2511.16203) · [PDF](https://arxiv.org/pdf/2511.16203.pdf)  
**作者**：Yuping Yan, Yuhan Xie, Yinxin Zhang, Lingjuan Lyu, Yaochu Jin  

**一句话要点**：提出VLA-Fool方法以评估具身视觉-语言-动作模型的多模态对抗鲁棒性

**关键词**：多模态对抗攻击, 视觉-语言-动作模型, 跨模态错位, 黑盒设置, 语义引导提示, 具身环境

## 3 点简述
- 核心问题：具身VLA模型在多模态和黑盒条件下的对抗鲁棒性未知，现有研究忽视跨模态错位影响
- 方法要点：统一文本、视觉和跨模态攻击，并引入语义引导提示框架增强攻击效果
- 实验或效果：在LIBERO基准上，微小多模态扰动可导致显著行为偏差，揭示模型脆弱性

## 摘要（原文）

> Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

