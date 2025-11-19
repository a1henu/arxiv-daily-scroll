---
layout: default
title: Automated glenoid bone loss measurement and segmentation in CT scans for pre-operative planning in shoulder instability
---

# Automated glenoid bone loss measurement and segmentation in CT scans for pre-operative planning in shoulder instability
**arXiv**：[2511.14083v1](https://arxiv.org/abs/2511.14083) · [PDF](https://arxiv.org/pdf/2511.14083.pdf)  
**作者**：Zhonghao Liu, Hanxue Gu, Qihang Li, Michael Fox, Jay M. Levin, Maciej A. Mazurowski, Brian C. Lau  

**一句话要点**：提出自动化深度学习管道以解决肩关节不稳术前规划中肩盂骨缺损测量问题

**关键词**：肩盂骨缺损测量, 深度学习管道, CT扫描分割, 几何拟合, 术前规划, 自动化评估

## 3 点简述
- 核心问题：手动和半自动测量肩盂骨缺损耗时且存在观察者间变异性。
- 方法要点：采用多阶段算法，包括U-Net分割、网络预测地标点和几何拟合计算骨缺损。
- 实验或效果：自动化测量与共识读数一致性强，ICC达0.84，优于外科医生间一致性。

## 摘要（原文）

> Reliable measurement of glenoid bone loss is essential for operative planning in shoulder instability, but current manual and semi-automated methods are time-consuming and often subject to interreader variability. We developed and validated a fully automated deep learning pipeline for measuring glenoid bone loss on three-dimensional computed tomography (CT) scans using a linear-based, en-face view, best-circle method. Shoulder CT images of 91 patients (average age, 40 years; range, 14-89 years; 65 men) were retrospectively collected along with manual labels including glenoid segmentation, landmarks, and bone loss measurements. The multi-stage algorithm has three main stages: (1) segmentation, where we developed a U-Net to automatically segment the glenoid and humerus; (2) anatomical landmark detection, where a second network predicts glenoid rim points; and (3) geometric fitting, where we applied principal component analysis (PCA), projection, and circle fitting to compute the percentage of bone loss. The automated measurements showed strong agreement with consensus readings and exceeded surgeon-to-surgeon consistency (intraclass correlation coefficient (ICC) 0.84 vs 0.78), including in low- and high-bone-loss subgroups (ICC 0.71 vs 0.63 and 0.83 vs 0.21, respectively; P < 0.001). For classifying patients into low, medium, and high bone-loss categories, the pipeline achieved a recall of 0.714 for low and 0.857 for high severity, with no low cases misclassified as high or vice versa. These results suggest that our method is a time-efficient and clinically reliable tool for preoperative planning in shoulder instability and for screening patients with substantial glenoid bone loss. Code and dataset are available at https://github.com/Edenliu1/Auto-Glenoid-Measurement-DL-Pipeline.

