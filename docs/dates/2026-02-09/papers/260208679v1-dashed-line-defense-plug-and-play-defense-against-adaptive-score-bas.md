---
layout: default
title: Dashed Line Defense: Plug-And-Play Defense Against Adaptive Score-Based Query Attacks
---

# Dashed Line Defense: Plug-And-Play Defense Against Adaptive Score-Based Query Attacks
**arXiv**：[2602.08679v1](https://arxiv.org/abs/2602.08679) · [PDF](https://arxiv.org/pdf/2602.08679.pdf)  
**作者**：Yanzhang Fu, Zizheng Guo, Jizhou Luo  

**一句话要点**：提出Dashed Line Defense以抵御自适应基于分数的查询攻击

**关键词**：对抗性攻击防御, 基于分数的查询攻击, 自适应攻击, 运行时防御, ImageNet

## 3 点简述
- 揭示现有运行时防御在自适应攻击下易被绕过，暴露关键局限性
- 提出Dashed Line Defense，通过引入损失模糊性干扰攻击者查询分析
- 在ImageNet上验证DLD优于先前防御，保持模型预测标签

## 摘要（原文）

> Score-based query attacks pose a serious threat to deep learning models by crafting adversarial examples (AEs) using only black-box access to model output scores, iteratively optimizing inputs based on observed loss values. While recent runtime defenses attempt to disrupt this process via output perturbation, most either require access to model parameters or fail when attackers adapt their tactics. In this paper, we first reveal that even the state-of-the-art plug-and-play defense can be bypassed by adaptive attacks, exposing a critical limitation of existing runtime defenses. We then propose Dashed Line Defense (DLD), a plug-and-play post-processing method specifically designed to withstand adaptive query strategies. By introducing ambiguity in how the observed loss reflects the true adversarial strength of candidate examples, DLD prevents attackers from reliably analyzing and adapting their queries, effectively disrupting the AE generation process. We provide theoretical guarantees of DLD's defense capability and validate its effectiveness through experiments on ImageNet, demonstrating that DLD consistently outperforms prior defenses--even under worst-case adaptive attacks--while preserving the model's predicted labels.

