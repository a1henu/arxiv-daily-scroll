---
layout: default
title: Automated HER2 scoring with uncertainty quantification using lensfree holography and deep learning
---

# Automated HER2 scoring with uncertainty quantification using lensfree holography and deep learning
**arXiv**：[2601.18219v1](https://arxiv.org/abs/2601.18219) · [PDF](https://arxiv.org/pdf/2601.18219.pdf)  
**作者**：Che-Yung Shen, Xilin Yang, Yuzhu Li, Leon Lenk, Aydogan Ozcan  

**一句话要点**：提出基于无透镜全息与深度学习的自动化HER2评分方法，适用于资源有限场景

**关键词**：无透镜全息成像, HER2评分, 不确定性量化, 深度学习, 乳腺癌诊断, 资源有限医疗

## 3 点简述
- 核心问题：传统数字HER2评分依赖笨重昂贵光学系统，难以在资源有限环境中应用
- 方法要点：集成紧凑无透镜全息平台与深度学习，通过贝叶斯蒙特卡洛dropout量化预测不确定性
- 实验或效果：在412个样本测试中，四类分类准确率84.9%，二元评分准确率94.8%，总体校正率30.4%

## 摘要（原文）

> Accurate assessment of human epidermal growth factor receptor 2 (HER2) expression is critical for breast cancer diagnosis, prognosis, and therapy selection; yet, most existing digital HER2 scoring methods rely on bulky and expensive optical systems. Here, we present a compact and cost-effective lensfree holography platform integrated with deep learning for automated HER2 scoring of immunohistochemically stained breast tissue sections. The system captures lensfree diffraction patterns of stained HER2 tissue sections under RGB laser illumination and acquires complex field information over a sample area of ~1,250 mm^2 at an effective throughput of ~84 mm^2 per minute. To enhance diagnostic reliability, we incorporated an uncertainty quantification strategy based on Bayesian Monte Carlo dropout, which provides autonomous uncertainty estimates for each prediction and supports reliable, robust HER2 scoring, with an overall correction rate of 30.4%. Using a blinded test set of 412 unique tissue samples, our approach achieved a testing accuracy of 84.9% for 4-class (0, 1+, 2+, 3+) HER2 classification and 94.8% for binary (0/1+ vs. 2+/3+) HER2 scoring with uncertainty quantification. Overall, this lensfree holography approach provides a practical pathway toward portable, high-throughput, and cost-effective HER2 scoring, particularly suited for resource-limited settings, where traditional digital pathology infrastructure is unavailable.

