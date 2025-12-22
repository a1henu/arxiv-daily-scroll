---
layout: default
title: Fose: Fusion of One-Step Diffusion and End-to-End Network for Pansharpening
---

# Fose: Fusion of One-Step Diffusion and End-to-End Network for Pansharpening
**arXiv**：[2512.17202v1](https://arxiv.org/abs/2512.17202) · [PDF](https://arxiv.org/pdf/2512.17202.pdf)  
**作者**：Kai Liu, Zeli Lin, Weibo Wang, Linghe Kong, Yulun Zhang  

**一句话要点**：提出Fose网络，融合一步扩散与端到端模型以提升全色锐化效率与性能。

**关键词**：全色锐化, 扩散模型, 端到端网络, 模型蒸馏, 图像融合, 轻量网络

## 3 点简述
- 核心问题：扩散模型计算耗时，端到端模型性能受限。
- 方法要点：通过四阶段训练策略，蒸馏扩散模型至一步，并与端到端模型轻量融合。
- 实验或效果：在三个基准测试中显著提升性能，推理速度比基线扩散模型快7.42倍。

## 摘要（原文）

> Pansharpening is a significant image fusion task that fuses low-resolution multispectral images (LRMSI) and high-resolution panchromatic images (PAN) to obtain high-resolution multispectral images (HRMSI). The development of the diffusion models (DM) and the end-to-end models (E2E model) has greatly improved the frontier of pansharping. DM takes the multi-step diffusion to obtain an accurate estimation of the residual between LRMSI and HRMSI. However, the multi-step process takes large computational power and is time-consuming. As for E2E models, their performance is still limited by the lack of prior and simple structure. In this paper, we propose a novel four-stage training strategy to obtain a lightweight network Fose, which fuses one-step DM and an E2E model. We perform one-step distillation on an enhanced SOTA DM for pansharping to compress the inference process from 50 steps to only 1 step. Then we fuse the E2E model with one-step DM with lightweight ensemble blocks. Comprehensive experiments are conducted to demonstrate the significant improvement of the proposed Fose on three commonly used benchmarks. Moreover, we achieve a 7.42 speedup ratio compared to the baseline DM while achieving much better performance. The code and model are released at https://github.com/Kai-Liu001/Fose.

