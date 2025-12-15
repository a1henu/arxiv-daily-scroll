---
layout: default
title: Maritime object classification with SAR imagery using quantum kernel methods
---

# Maritime object classification with SAR imagery using quantum kernel methods
**arXiv**：[2512.11367v1](https://arxiv.org/abs/2512.11367) · [PDF](https://arxiv.org/pdf/2512.11367.pdf)  
**作者**：John Tanner, Nicholas Davies, Pascal Elahi, Casey R. Myers, Du Huynh, Wei Liu, Mark Reynolds, Jingbo Wang  

**一句话要点**：提出量子核方法用于SAR图像海事目标分类，评估其在船舶与非船舶及渔船分类中的性能。

**关键词**：量子机器学习, 合成孔径雷达, 海事目标分类, 量子核方法, SARFish数据集

## 3 点简述
- 核心问题：SAR图像中非法捕鱼等海事目标分类困难，需全天候监测。
- 方法要点：应用量子核方法处理SARFish数据集中的实数和复数SAR芯片。
- 实验或效果：量子核方法在无噪声模拟中性能与经典核相当或更优，但复数数据未显优势。

## 摘要（原文）

> Illegal, unreported, and unregulated (IUU) fishing causes global economic losses of \$10-25 billion annually and undermines marine sustainability and governance. Synthetic Aperture Radar (SAR) provides reliable maritime surveillance under all weather and lighting conditions, but classifying small maritime objects in SAR imagery remains challenging. We investigate quantum machine learning for this task, focusing on Quantum Kernel Methods (QKMs) applied to real and complex SAR chips extracted from the SARFish dataset. We tackle two binary classification problems, the first for distinguishing vessels from non-vessels, and the second for distinguishing fishing vessels from other types of vessels. We compare QKMs applied to real and complex SAR chips against classical Laplacian, RBF, and linear kernels applied to real SAR chips. Using noiseless numerical simulations of the quantum kernels, we find that QKMs are capable of obtaining equal or better performance than the classical kernel on these tasks in the best case, but do not demonstrate a clear advantage for the complex SAR data. This work presents the first application of QKMs to maritime classification in SAR imagery and offers insight into the potential and current limitations of quantum-enhanced learning for maritime surveillance.

