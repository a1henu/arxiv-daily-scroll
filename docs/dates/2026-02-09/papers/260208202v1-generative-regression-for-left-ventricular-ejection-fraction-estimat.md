---
layout: default
title: Generative Regression for Left Ventricular Ejection Fraction Estimation from Echocardiography Video
---

# Generative Regression for Left Ventricular Ejection Fraction Estimation from Echocardiography Video
**arXiv**：[2602.08202v1](https://arxiv.org/abs/2602.08202) · [PDF](https://arxiv.org/pdf/2602.08202.pdf)  
**作者**：Jinrong Lv, Xun Gong, Zhaohuan Li, Weili Jiang  

**一句话要点**：提出MCSDR生成回归模型，用于从超声心动图视频估计左心室射血分数，以解决后验分布多模态问题。

**关键词**：生成回归, 左心室射血分数估计, 超声心动图视频分析, 条件分数扩散模型, 多模态后验分布, AI辅助诊断

## 3 点简述
- 核心问题：超声心动图视频估计LVEF存在噪声和视角限制，导致后验分布多模态，传统回归方法可能产生误导预测。
- 方法要点：采用生成回归范式，提出MCSDR模型，基于条件分数扩散建模连续后验分布，结合视频和患者属性先验。
- 实验或效果：在EchoNet-Dynamic等数据集上实现SOTA性能，生成轨迹在噪声或生理变异大时提供可解释性。

## 摘要（原文）

> Estimating Left Ventricular Ejection Fraction (LVEF) from echocardiograms constitutes an ill-posed inverse problem. Inherent noise, artifacts, and limited viewing angles introduce ambiguity, where a single video sequence may map not to a unique ground truth, but rather to a distribution of plausible physiological values. Prevailing deep learning approaches typically formulate this task as a standard regression problem that minimizes the Mean Squared Error (MSE). However, this paradigm compels the model to learn the conditional expectation, which may yield misleading predictions when the underlying posterior distribution is multimodal or heavy-tailed -- a common phenomenon in pathological scenarios. In this paper, we investigate the paradigm shift from deterministic regression toward generative regression. We propose the Multimodal Conditional Score-based Diffusion model for Regression (MCSDR), a probabilistic framework designed to model the continuous posterior distribution of LVEF conditioned on echocardiogram videos and patient demographic attribute priors. Extensive experiments conducted on the EchoNet-Dynamic, EchoNet-Pediatric, and CAMUS datasets demonstrate that MCSDR achieves state-of-the-art performance. Notably, qualitative analysis reveals that the generation trajectories of our model exhibit distinct behaviors in cases characterized by high noise or significant physiological variability, thereby offering a novel layer of interpretability for AI-aided diagnosis.

