---
layout: default
title: Diffusion Model's Generalization Can Be Characterized by Inductive Biases toward a Data-Dependent Ridge Manifold
---

# Diffusion Model's Generalization Can Be Characterized by Inductive Biases toward a Data-Dependent Ridge Manifold
**arXiv**：[2602.06021v1](https://arxiv.org/abs/2602.06021) · [PDF](https://arxiv.org/pdf/2602.06021.pdf)  
**作者**：Ye He, Yitong Qiu, Molei Tao  

**一句话要点**：提出数据依赖脊流形以量化扩散模型的泛化行为，揭示推理动态的到达-对齐-滑动过程。

**关键词**：扩散模型, 泛化分析, 脊流形, 推理动态, 数据依赖, 多模态生成

## 3 点简述
- 核心问题：扩散模型在非记忆训练数据时如何泛化，影响下游应用评估。
- 方法要点：通过脊流形量化生成数据关系，分析推理中的到达-对齐-滑动动态。
- 实验或效果：在合成多模态分布和MNIST潜在扩散中验证方向效应，支持理论预测。

## 摘要（原文）

> When a diffusion model is not memorizing the training data set, how does it generalize exactly? A quantitative understanding of the distribution it generates would be beneficial to, for example, an assessment of the model's performance for downstream applications. We thus explicitly characterize what diffusion model generates, by proposing a log-density ridge manifold and quantifying how the generated data relate to this manifold as inference dynamics progresses. More precisely, inference undergoes a reach-align-slide process centered around the ridge manifold: trajectories first reach a neighborhood of the manifold, then align as being pushed toward or away from the manifold in normal directions, and finally slide along the manifold in tangent directions. Within the scope of this general behavior, different training errors will lead to different normal and tangent motions, which can be quantified, and these detailed motions characterize when inter-mode generations emerge. More detailed understanding of training dynamics will lead to more accurate quantification of the generation inductive bias, and an example of random feature model will be considered, for which we can explicitly illustrate how diffusion model's inductive biases originate as a composition of architectural bias and training accuracy, and how they evolve with the inference dynamics. Experiments on synthetic multimodal distributions and MNIST latent diffusion support the predicted directional effects, in both low- and high-dimensions.

