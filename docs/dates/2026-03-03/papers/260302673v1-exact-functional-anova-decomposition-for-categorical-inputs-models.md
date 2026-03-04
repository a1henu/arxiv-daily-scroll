---
layout: default
title: Exact Functional ANOVA Decomposition for Categorical Inputs Models
---

# Exact Functional ANOVA Decomposition for Categorical Inputs Models
**arXiv**：[2603.02673v1](https://arxiv.org/abs/2603.02673) · [PDF](https://arxiv.org/pdf/2603.02673.pdf)  
**作者**：Baptiste Ferrere, Nicolas Bousquet, Fabrice Gamboa, Jean-Michel Loubes, Joseph Muré  

**一句话要点**：提出闭式函数ANOVA分解以解决分类输入模型在依赖分布下的可解释性问题

**关键词**：函数ANOVA分解, 分类输入模型, 可解释性, SHAP值, 依赖分布, 闭式解

## 3 点简述
- 核心问题：依赖分布下函数ANOVA分解缺乏闭式解，依赖采样近似计算成本高
- 方法要点：结合泛函分析与离散傅里叶分析，推导出无假设的闭式分解公式
- 实验或效果：公式计算高效，适用于任意依赖结构，推广了SHAP值

## 摘要（原文）

> Functional ANOVA offers a principled framework for interpretability by decomposing a model's prediction into main effects and higher-order interactions. For independent features, this decomposition is well-defined, strongly linked with SHAP values, and serves as a cornerstone of additive explainability. However, the lack of an explicit closed-form expression for general dependent distributions has forced practitioners to rely on costly sampling-based approximations. We completely resolve this limitation for categorical inputs. By bridging functional analysis with the extension of discrete Fourier analysis, we derive a closed-form decomposition without any assumption. Our formulation is computationally very efficient. It seamlessly recovers the classical independent case and extends to arbitrary dependence structures, including distributions with non-rectangular support. Furthermore, leveraging the intrinsic link between SHAP and ANOVA under independence, our framework yields a natural generalization of SHAP values for the general categorical setting.

