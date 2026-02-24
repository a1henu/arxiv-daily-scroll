---
layout: default
title: JUCAL: Jointly Calibrating Aleatoric and Epistemic Uncertainty in Classification Tasks
---

# JUCAL: Jointly Calibrating Aleatoric and Epistemic Uncertainty in Classification Tasks
**arXiv**：[2602.20153v1](https://arxiv.org/abs/2602.20153) · [PDF](https://arxiv.org/pdf/2602.20153.pdf)  
**作者**：Jakob Heiss, Sören Lambrecht, Jakob Weissteiner, Hanna Wutte, Žan Žurič, Josef Teichmann, Bin Yu  

**一句话要点**：提出JUCAL联合校准分类任务中的偶然与认知不确定性，以平衡不确定性比例。

**关键词**：不确定性校准, 分类任务, 集成学习, 负对数似然, 预测不确定性

## 3 点简述
- 核心问题：现有校准方法未平衡偶然与认知不确定性，导致预测不确定性误判。
- 方法要点：JUCAL通过优化负对数似然联合校准两个常数，加权和缩放两种不确定性。
- 实验或效果：在文本分类任务中显著优于SOTA方法，降低NLL和预测集大小，减少推理成本。

## 摘要（原文）

> We study post-calibration uncertainty for trained ensembles of classifiers. Specifically, we consider both aleatoric (label noise) and epistemic (model) uncertainty. Among the most popular and widely used calibration methods in classification are temperature scaling (i.e., pool-then-calibrate) and conformal methods. However, the main shortcoming of these calibration methods is that they do not balance the proportion of aleatoric and epistemic uncertainty. Not balancing these uncertainties can severely misrepresent predictive uncertainty, leading to overconfident predictions in some input regions while being underconfident in others. To address this shortcoming, we present a simple but powerful calibration algorithm Joint Uncertainty Calibration (JUCAL) that jointly calibrates aleatoric and epistemic uncertainty. JUCAL jointly calibrates two constants to weight and scale epistemic and aleatoric uncertainties by optimizing the negative log-likelihood (NLL) on the validation/calibration dataset. JUCAL can be applied to any trained ensemble of classifiers (e.g., transformers, CNNs, or tree-based methods), with minimal computational overhead, without requiring access to the models' internal parameters. We experimentally evaluate JUCAL on various text classification tasks, for ensembles of varying sizes and with different ensembling strategies. Our experiments show that JUCAL significantly outperforms SOTA calibration methods across all considered classification tasks, reducing NLL and predictive set size by up to 15% and 20%, respectively. Interestingly, even applying JUCAL to an ensemble of size 5 can outperform temperature-scaled ensembles of size up to 50 in terms of NLL and predictive set size, resulting in up to 10 times smaller inference costs. Thus, we propose JUCAL as a new go-to method for calibrating ensembles in classification.

