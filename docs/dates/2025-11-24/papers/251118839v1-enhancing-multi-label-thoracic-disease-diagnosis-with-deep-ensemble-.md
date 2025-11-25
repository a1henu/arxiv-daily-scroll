---
layout: default
title: Enhancing Multi-Label Thoracic Disease Diagnosis with Deep Ensemble-Based Uncertainty Quantification
---

# Enhancing Multi-Label Thoracic Disease Diagnosis with Deep Ensemble-Based Uncertainty Quantification
**arXiv**：[2511.18839v1](https://arxiv.org/abs/2511.18839) · [PDF](https://arxiv.org/pdf/2511.18839.pdf)  
**作者**：Yasiru Laksara, Uthayasanker Thayasivam  

**一句话要点**：提出基于深度集成的不确定性量化方法，以增强多标签胸部疾病诊断的可靠性

**关键词**：不确定性量化, 深度集成, 胸部X光诊断, 多标签分类, 模型校准, 临床决策支持

## 3 点简述
- 核心问题：深度学习模型在临床应用中缺乏可靠的不确定性度量，影响决策可信度
- 方法要点：采用9成员深度集成替代蒙特卡洛Dropout，实现不确定性分解与性能稳定
- 实验或效果：在NIH ChestX-ray14数据集上达到SOTA AUROC 0.8559，平均ECE 0.0728

## 摘要（原文）

> The utility of deep learning models, such as CheXNet, in high stakes clinical settings is fundamentally constrained by their purely deterministic nature, failing to provide reliable measures of predictive confidence. This project addresses this critical gap by integrating robust Uncertainty Quantification (UQ) into a high performance diagnostic platform for 14 common thoracic diseases on the NIH ChestX-ray14 dataset. Initial architectural development failed to stabilize performance and calibration using Monte Carlo Dropout (MCD), yielding an unacceptable Expected Calibration Error (ECE) of 0.7588. This technical failure necessitated a rigorous architectural pivot to a high diversity, 9-member Deep Ensemble (DE). This resulting DE successfully stabilized performance and delivered superior reliability, achieving a State-of-the-Art (SOTA) average Area Under the Receiver Operating Characteristic Curve (AUROC) of 0.8559 and an average F1 Score of 0.3857. Crucially, the DE demonstrated superior calibration (Mean ECE of 0.0728 and Negative Log-Likelihood (NLL) of 0.1916) and enabled the reliable decomposition of total uncertainty into its Aleatoric (irreducible data noise) and Epistemic (reducible model knowledge) components, with a mean Epistemic Uncertainty (EU) of 0.0240. These results establish the Deep Ensemble as a trustworthy and explainable platform, transforming the model from a probabilistic tool into a reliable clinical decision support system.

