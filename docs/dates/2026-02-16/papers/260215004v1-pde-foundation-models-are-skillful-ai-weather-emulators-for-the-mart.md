---
layout: default
title: PDE foundation models are skillful AI weather emulators for the Martian atmosphere
---

# PDE foundation models are skillful AI weather emulators for the Martian atmosphere
**arXiv**：[2602.15004v1](https://arxiv.org/abs/2602.15004) · [PDF](https://arxiv.org/pdf/2602.15004.pdf)  
**作者**：Johannes Schmude, Sujit Roy, Liping Wang, Theodore van Kessel, Levente Klein, Marcus Freitag, Eloisa Bentivegna, Robert Manson-Sawko, Bjorn Lutjens, Manil Maskey, Campbell Watson, Rahul Ramachandran, Juan Bernabe-Moreno  

**一句话要点**：提出基于PDE基础模型的三维火星大气天气模拟器，通过预训练与扩展提升预测性能。

**关键词**：PDE基础模型, 火星大气模拟, 三维扩展, 稀疏初始条件, AI天气预测, 预训练微调

## 3 点简述
- 核心问题：火星大气天气模拟面临训练数据不足或计算资源有限，需高效AI模型。
- 方法要点：扩展Poseidon PDE基础模型从二维到三维，保持预训练信息，适应稀疏初始条件。
- 实验或效果：使用34 GB数据训练，计算预算13 GPU小时，在测试集上性能提升34.4%。

## 摘要（原文）

> We show that AI foundation models that are pretrained on numerical solutions to a diverse corpus of partial differential equations can be adapted and fine-tuned to obtain skillful predictive weather emulators for the Martian atmosphere. We base our work on the Poseidon PDE foundation model for two-dimensional systems. We develop a method to extend Poseidon from two to three dimensions while keeping the pretraining information. Moreover, we investigate the performance of the model in the presence of sparse initial conditions. Our results make use of four Martian years (approx.~34 GB) of training data and a median compute budget of 13 GPU hours. We find that the combination of pretraining and model extension yields a performance increase of 34.4\% on a held-out year. This shows that PDEs-FMs can not only approximate solutions to (other) PDEs but also anchor models for real-world problems with complex interactions that lack a sufficient amount of training data or a suitable compute budget.

