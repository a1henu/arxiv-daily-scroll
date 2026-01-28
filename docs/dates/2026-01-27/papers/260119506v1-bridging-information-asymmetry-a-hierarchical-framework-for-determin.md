---
layout: default
title: Bridging Information Asymmetry: A Hierarchical Framework for Deterministic Blind Face Restoration
---

# Bridging Information Asymmetry: A Hierarchical Framework for Deterministic Blind Face Restoration
**arXiv**：[2601.19506v1](https://arxiv.org/abs/2601.19506) · [PDF](https://arxiv.org/pdf/2601.19506.pdf)  
**作者**：Zhengjian Yao, Jiakui Hu, Kaiwen Li, Hangzhou He, Xinliang Zhang, Shuang Zeng, Lei Zhu, Yanye Lu  

**一句话要点**：提出Pref-Restore分层框架以解决盲人脸恢复中的信息不对称问题，实现确定性恢复。

**关键词**：盲人脸恢复, 信息不对称, 分层框架, 确定性恢复, 偏好对齐, 扩散模型

## 3 点简述
- 核心问题：盲人脸恢复因信息不对称导致随机不确定性和幻觉伪影。
- 方法要点：通过增强输入密度和修剪输出分布，结合语义逻辑与纹理生成。
- 实验或效果：在合成和真实基准测试中达到先进性能，显著降低解熵。

## 摘要（原文）

> Blind face restoration remains a persistent challenge due to the inherent ill-posedness of reconstructing holistic structures from severely constrained observations. Current generative approaches, while capable of synthesizing realistic textures, often suffer from information asymmetry -- the intrinsic disparity between the information-sparse low quality inputs and the information-dense high quality outputs. This imbalance leads to a one-to-many mapping, where insufficient constraints result in stochastic uncertainty and hallucinatory artifacts. To bridge this gap, we present \textbf{Pref-Restore}, a hierarchical framework that integrates discrete semantic logic with continuous texture generation to achieve deterministic, preference-aligned restoration. Our methodology fundamentally addresses this information disparity through two complementary strategies: (1) Augmenting Input Density: We employ an auto-regressive integrator to reformulate textual instructions into dense latent queries, injecting high-level semantic stability to constrain the degraded signals; (2) Pruning Output Distribution: We pioneer the integration of on-policy reinforcement learning directly into the diffusion restoration loop. By transforming human preferences into differentiable constraints, we explicitly penalize stochastic deviations, thereby sharpening the posterior distribution toward the desired high-fidelity outcomes. Extensive experiments demonstrate that Pref-Restore achieves state-of-the-art performance across synthetic and real-world benchmarks. Furthermore, empirical analysis confirms that our preference-aligned strategy significantly reduces solution entropy, establishing a robust pathway toward reliable and deterministic blind restoration.

