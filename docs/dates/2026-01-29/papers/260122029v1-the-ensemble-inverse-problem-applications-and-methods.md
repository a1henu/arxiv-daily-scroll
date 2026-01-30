---
layout: default
title: The Ensemble Inverse Problem: Applications and Methods
---

# The Ensemble Inverse Problem: Applications and Methods
**arXiv**：[2601.22029v1](https://arxiv.org/abs/2601.22029) · [PDF](https://arxiv.org/pdf/2601.22029.pdf)  
**作者**：Zhengyan Huan, Camila Pazos, Martin Klassen, Vincent Croft, Pierre-Hugues Beauchemin, Shuchin Aeron  

**一句话要点**：提出集合逆问题及其非迭代推理方法，应用于高能物理、全波形反演和逆成像

**关键词**：集合逆问题, 条件生成模型, 非迭代推理, 高能物理, 全波形反演, 逆成像

## 3 点简述
- 定义集合逆问题，旨在从观测数据反演先验分布的前向过程推演集合
- 提出基于条件生成模型的非迭代后验采样器，利用观测集合信息避免推理时显式迭代前向模型
- 在合成和真实数据集上验证方法，支持泛化到未见先验，代码已开源

## 摘要（原文）

> We introduce a new multivariate statistical problem that we refer to as the Ensemble Inverse Problem (EIP). The aim of EIP is to invert for an ensemble that is distributed according to the pushforward of a prior under a forward process. In high energy physics (HEP), this is related to a widely known problem called unfolding, which aims to reconstruct the true physics distribution of quantities, such as momentum and angle, from measurements that are distorted by detector effects. In recent applications, the EIP also arises in full waveform inversion (FWI) and inverse imaging with unknown priors. We propose non-iterative inference-time methods that construct posterior samplers based on a new class of conditional generative models, which we call ensemble inverse generative models. For the posterior modeling, these models additionally use the ensemble information contained in the observation set on top of single measurements. Unlike existing methods, our proposed methods avoid explicit and iterative use of the forward model at inference time via training across several sets of truth-observation pairs that are consistent with the same forward model, but originate from a wide range of priors. We demonstrate that this training procedure implicitly encodes the likelihood model. The use of ensemble information helps posterior inference and enables generalization to unseen priors. We benchmark the proposed method on several synthetic and real datasets in inverse imaging, HEP, and FWI. The codes are available at https://github.com/ZhengyanHuan/The-Ensemble-Inverse-Problem--Applications-and-Methods.

