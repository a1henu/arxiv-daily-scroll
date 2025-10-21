---
layout: default
title: Investigating Adversarial Robustness against Preprocessing used in Blackbox Face Recognition
---

# Investigating Adversarial Robustness against Preprocessing used in Blackbox Face Recognition
**arXiv**：[2510.17169v1](https://arxiv.org/abs/2510.17169) · [PDF](https://arxiv.org/pdf/2510.17169.pdf)  
**作者**：Roland Croft, Brian Du, Darcy Joseph, Sharath Kumar  

**一句话要点**：提出预处理不变方法以提升黑盒人脸识别中对抗攻击的迁移性

**关键词**：人脸识别, 对抗攻击, 黑盒设置, 预处理技术, 迁移性提升

## 3 点简述
- 核心问题：黑盒人脸识别系统中预处理常被忽视，影响对抗攻击迁移性。
- 方法要点：使用输入变换构建预处理不变方法，增强攻击鲁棒性。
- 实验或效果：攻击成功率提升达27%，预处理选择可降低成功率78%。

## 摘要（原文）

> Face Recognition (FR) models have been shown to be vulnerable to adversarial
> examples that subtly alter benign facial images, exposing blind spots in these
> systems, as well as protecting user privacy. End-to-end FR systems first obtain
> preprocessed faces from diverse facial imagery prior to computing the
> similarity of the deep feature embeddings. Whilst face preprocessing is a
> critical component of FR systems, and hence adversarial attacks against them,
> we observe that this preprocessing is often overlooked in blackbox settings.
> Our study seeks to investigate the transferability of several out-of-the-box
> state-of-the-art adversarial attacks against FR when applied against different
> preprocessing techniques used in a blackbox setting. We observe that the choice
> of face detection model can degrade the attack success rate by up to 78%,
> whereas choice of interpolation method during downsampling has relatively
> minimal impacts. Furthermore, we find that the requirement for facial
> preprocessing even degrades attack strength in a whitebox setting, due to the
> unintended interaction of produced noise vectors against face detection models.
> Based on these findings, we propose a preprocessing-invariant method using
> input transformations that improves the transferability of the studied attacks
> by up to 27%. Our findings highlight the importance of preprocessing in FR
> systems, and the need for its consideration towards improving the adversarial
> generalisation of facial adversarial examples.

