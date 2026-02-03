---
layout: default
title: MIRROR: Manifold Ideal Reference ReconstructOR for Generalizable AI-Generated Image Detection
---

# MIRROR: Manifold Ideal Reference ReconstructOR for Generalizable AI-Generated Image Detection
**arXiv**：[2602.02222v1](https://arxiv.org/abs/2602.02222) · [PDF](https://arxiv.org/pdf/2602.02222.pdf)  
**作者**：Ruiqi Liu, Manni Cui, Ziheng Qin, Zhiyuan Yan, Ruoxin Chen, Yi Han, Zhiheng Li, Junkai Chen, ZhiJin Chen, Kaiqing Lin, Jialiang Shen, Lubin Weng, Jing Dong, Yan Wang, Shu Wu  

**一句话要点**：提出MIRROR框架，通过流形一致性参考重构解决AI生成图像检测的泛化性问题。

**关键词**：AI生成图像检测, 流形学习, 参考比较, 泛化性, 人类认知基准

## 3 点简述
- 核心问题：高保真生成模型缩小了合成与真实图像的感知差距，现有基于伪影的分类方法难以泛化到演化的生成痕迹。
- 方法要点：将检测重构为参考比较问题，使用可学习离散记忆库编码现实先验，通过稀疏线性组合投影输入到流形一致理想参考。
- 实验或效果：在14个基准测试中表现优异，在Human-AIGI基准上达到89.6%准确率，超越人类用户和视觉专家。

## 摘要（原文）

> High-fidelity generative models have narrowed the perceptual gap between synthetic and real images, posing serious threats to media security. Most existing AI-generated image (AIGI) detectors rely on artifact-based classification and struggle to generalize to evolving generative traces. In contrast, human judgment relies on stable real-world regularities, with deviations from the human cognitive manifold serving as a more generalizable signal of forgery. Motivated by this insight, we reformulate AIGI detection as a Reference-Comparison problem that verifies consistency with the real-image manifold rather than fitting specific forgery cues. We propose MIRROR (Manifold Ideal Reference ReconstructOR), a framework that explicitly encodes reality priors using a learnable discrete memory bank. MIRROR projects an input into a manifold-consistent ideal reference via sparse linear combination, and uses the resulting residuals as robust detection signals. To evaluate whether detectors reach the "superhuman crossover" required to replace human experts, we introduce the Human-AIGI benchmark, featuring a psychophysically curated human-imperceptible subset. Across 14 benchmarks, MIRROR consistently outperforms prior methods, achieving gains of 2.1% on six standard benchmarks and 8.1% on seven in-the-wild benchmarks. On Human-AIGI, MIRROR reaches 89.6% accuracy across 27 generators, surpassing both lay users and visual experts, and further approaching the human perceptual limit as pretrained backbones scale. The code is publicly available at: https://github.com/349793927/MIRROR

