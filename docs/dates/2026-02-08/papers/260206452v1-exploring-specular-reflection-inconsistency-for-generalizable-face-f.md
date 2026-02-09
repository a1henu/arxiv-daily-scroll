---
layout: default
title: Exploring Specular Reflection Inconsistency for Generalizable Face Forgery Detection
---

# Exploring Specular Reflection Inconsistency for Generalizable Face Forgery Detection
**arXiv**：[2602.06452v1](https://arxiv.org/abs/2602.06452) · [PDF](https://arxiv.org/pdf/2602.06452.pdf)  
**作者**：Hongyan Fei, Zexi Jia, Chuanwei Huang, Jinchao Zhang, Jie Zhou  

**一句话要点**：提出基于镜面反射不一致性的可泛化人脸伪造检测方法SRI-Net

**关键词**：人脸伪造检测, 镜面反射不一致性, Retinex理论, 两阶段交叉注意力, 可泛化检测, 扩散模型伪造

## 3 点简述
- 针对AI生成高质量伪造人脸检测难题，聚焦镜面反射物理属性难以复现的特性
- 基于Retinex理论快速估计人脸纹理，分离镜面反射，设计两阶段交叉注意力网络捕获不一致性
- 在传统和生成式伪造数据集上表现优异，尤其对扩散模型生成伪造有效

## 摘要（原文）

> Detecting deepfakes has become increasingly challenging as forgery faces synthesized by AI-generated methods, particularly diffusion models, achieve unprecedented quality and resolution. Existing forgery detection approaches relying on spatial and frequency features demonstrate limited efficacy against high-quality, entirely synthesized forgeries. In this paper, we propose a novel detection method grounded in the observation that facial attributes governed by complex physical laws and multiple parameters are inherently difficult to replicate. Specifically, we focus on illumination, particularly the specular reflection component in the Phong illumination model, which poses the greatest replication challenge due to its parametric complexity and nonlinear formulation. We introduce a fast and accurate face texture estimation method based on Retinex theory to enable precise specular reflection separation. Furthermore, drawing from the mathematical formulation of specular reflection, we posit that forgery evidence manifests not only in the specular reflection itself but also in its relationship with corresponding face texture and direct light. To address this issue, we design the Specular-Reflection-Inconsistency-Network (SRI-Net), incorporating a two-stage cross-attention mechanism to capture these correlations and integrate specular reflection related features with image features for robust forgery detection. Experimental results demonstrate that our method achieves superior performance on both traditional deepfake datasets and generative deepfake datasets, particularly those containing diffusion-generated forgery faces.

