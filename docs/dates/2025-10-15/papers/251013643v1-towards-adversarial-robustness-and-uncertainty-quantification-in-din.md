---
layout: default
title: Towards Adversarial Robustness and Uncertainty Quantification in DINOv2-based Few-Shot Anomaly Detection
---

# Towards Adversarial Robustness and Uncertainty Quantification in DINOv2-based Few-Shot Anomaly Detection
**arXiv**：[2510.13643v1](https://arxiv.org/abs/2510.13643) · [PDF](https://arxiv.org/pdf/2510.13643.pdf)  
**作者**：Akib Mohammed Khan, Bartosz Krawczyk  

**一句话要点**：评估DINOv2小样本异常检测的对抗鲁棒性和不确定性量化，提出后处理校准基线

**关键词**：异常检测, 对抗攻击, 不确定性量化, DINOv2模型, 小样本学习, 模型校准

## 3 点简述
- 核心问题：DINOv2基础模型在异常检测中易受对抗攻击且不确定性校准不足
- 方法要点：使用冻结DINOv2特征附加线性头进行白盒攻击，并应用Platt缩放校准异常分数
- 实验或效果：在MVTec-AD和VisA数据集上，FGSM攻击导致性能下降，校准后熵增加并降低校准误差

## 摘要（原文）

> Foundation models such as DINOv2 have shown strong performance in few-shot
> anomaly detection, yet two key questions remain unexamined: (i) how susceptible
> are these detectors to adversarial perturbations; and (ii) how well do their
> anomaly scores reflect calibrated uncertainty? Building on AnomalyDINO, a
> training-free deep nearest-neighbor detector over DINOv2 features, we present
> one of the first systematic studies of adversarial attacks and uncertainty
> estimation in this setting. To enable white-box gradient attacks while
> preserving test-time behavior, we attach a lightweight linear head to frozen
> DINOv2 features only for crafting perturbations. Using this heuristic, we
> evaluate the impact of FGSM across the MVTec-AD and VisA datasets and observe
> consistent drops in F1, AUROC, AP, and G-mean, indicating that imperceptible
> perturbations can flip nearest-neighbor relations in feature space to induce
> confident misclassification. Complementing robustness, we probe reliability and
> find that raw anomaly scores are poorly calibrated, revealing a gap between
> confidence and correctness that limits safety-critical use. As a simple, strong
> baseline toward trustworthiness, we apply post-hoc Platt scaling to the anomaly
> scores for uncertainty estimation. The resulting calibrated posteriors yield
> significantly higher predictive entropy on adversarially perturbed inputs than
> on clean ones, enabling a practical flagging mechanism for attack detection
> while reducing calibration error (ECE). Our findings surface concrete
> vulnerabilities in DINOv2-based few-shot anomaly detectors and establish an
> evaluation protocol and baseline for robust, uncertainty-aware anomaly
> detection. We argue that adversarial robustness and principled uncertainty
> quantification are not optional add-ons but essential capabilities if anomaly
> detection systems are to be trustworthy and ready for real-world deployment.

