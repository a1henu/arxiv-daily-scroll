---
layout: default
title: Orientation-Robust Latent Motion Trajectory Learning for Annotation-free Cardiac Phase Detection in Fetal Echocardiography
---

# Orientation-Robust Latent Motion Trajectory Learning for Annotation-free Cardiac Phase Detection in Fetal Echocardiography
**arXiv**：[2602.06761v1](https://arxiv.org/abs/2602.06761) · [PDF](https://arxiv.org/pdf/2602.06761.pdf)  
**作者**：Yingyu Yang, Qianye Yang, Can Peng, Elena D'Alberti, Olga Patey, Aris T. Papageorghiou, J. Alison Noble  

**一句话要点**：提出ORBIT框架以解决胎儿超声心动图中无标注心脏相位检测的方位鲁棒性问题

**关键词**：胎儿超声心动图, 心脏相位检测, 自监督学习, 方位鲁棒性, 潜在运动轨迹

## 3 点简述
- 核心问题：胎儿超声心动图缺乏心电图信号，手动识别舒张末期和收缩末期帧耗时且依赖胎儿心脏方位。
- 方法要点：通过配准作为自监督任务，学习心脏形变的潜在运动轨迹，利用转折点捕获相位转换。
- 实验或效果：在正常和先天性心脏病病例上均表现一致，平均绝对误差优于现有无标注方法。

## 摘要（原文）

> Fetal echocardiography is essential for detecting congenital heart disease (CHD), facilitating pregnancy management, optimized delivery planning, and timely postnatal interventions. Among standard imaging planes, the four-chamber (4CH) view provides comprehensive information for CHD diagnosis, where clinicians carefully inspect the end-diastolic (ED) and end-systolic (ES) phases to evaluate cardiac structure and motion. Automated detection of these cardiac phases is thus a critical component toward fully automated CHD analysis. Yet, in the absence of fetal electrocardiography (ECG), manual identification of ED and ES frames remains a labor-intensive bottleneck. We present ORBIT (Orientation-Robust Beat Inference from Trajectories), a self-supervised framework that identifies cardiac phases without manual annotations under various fetal heart orientation. ORBIT employs registration as self-supervision task and learns a latent motion trajectory of cardiac deformation, whose turning points capture transitions between cardiac relaxation and contraction, enabling accurate and orientation-robust localization of ED and ES frames across diverse fetal positions. Trained exclusively on normal fetal echocardiography videos, ORBIT achieves consistent performance on both normal (MAE = 1.9 frames for ED and 1.6 for ES) and CHD cases (MAE = 2.4 frames for ED and 2.1 for ES), outperforming existing annotation-free approaches constrained by fixed orientation assumptions. These results highlight the potential of ORBIT to facilitate robust cardiac phase detection directly from 4CH fetal echocardiography.

