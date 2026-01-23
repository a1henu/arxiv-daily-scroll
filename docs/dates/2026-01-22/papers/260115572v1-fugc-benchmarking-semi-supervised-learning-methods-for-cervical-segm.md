---
layout: default
title: FUGC: Benchmarking Semi-Supervised Learning Methods for Cervical Segmentation
---

# FUGC: Benchmarking Semi-Supervised Learning Methods for Cervical Segmentation
**arXiv**：[2601.15572v1](https://arxiv.org/abs/2601.15572) · [PDF](https://arxiv.org/pdf/2601.15572.pdf)  
**作者**：Jieyun Bai, Yitong Tang, Zihao Zhou, Mahdi Islam, Musarrat Tabassum, Enrique Almar-Munoz, Hongyu Liu, Hui Meng, Nianjiang Lv, Bo Deng, Yu Chen, Zilun Peng, Yusong Xiao, Li Xiao, Nam-Khanh Tran, Dac-Phu Phan-Le, Hai-Dang Nguyen, Xiao Liu, Jiale Hu, Mingxu Huang, Jitao Liang, Chaolu Feng, Xuezhi Zhang, Lyuyang Tong, Bo Du, Ha-Hieu Pham, Thanh-Huy Nguyen, Min Xu, Juntao Jiang, Jiangning Zhang, Yong Liu, Md. Kamrul Hasan, Jie Gan, Zhuonan Liang, Weidong Cai, Yuxin Huang, Gongning Luo, Mohammad Yaqub, Karim Lekadir  

**一句话要点**：提出FUGC基准以解决宫颈分割中标注数据稀缺问题，推动半监督学习方法评估。

**关键词**：宫颈分割, 半监督学习, 超声图像, 早产风险评估, 基准测试, 医学图像分析

## 3 点简述
- 核心问题：经阴道超声图像中宫颈结构分割对早产风险评估至关重要，但标注数据稀缺限制监督学习性能。
- 方法要点：建立首个宫颈分割半监督学习基准，提供890张图像数据集，包括训练、验证和测试集。
- 实验或效果：评估10个团队的解决方案，最佳方法在DSC、HD和RT指标上分别达到90.26%、38.88毫米和32.85毫秒。

## 摘要（原文）

> Accurate segmentation of cervical structures in transvaginal ultrasound (TVS) is critical for assessing the risk of spontaneous preterm birth (PTB), yet the scarcity of labeled data limits the performance of supervised learning approaches. This paper introduces the Fetal Ultrasound Grand Challenge (FUGC), the first benchmark for semi-supervised learning in cervical segmentation, hosted at ISBI 2025. FUGC provides a dataset of 890 TVS images, including 500 training images, 90 validation images, and 300 test images. Methods were evaluated using the Dice Similarity Coefficient (DSC), Hausdorff Distance (HD), and runtime (RT), with a weighted combination of 0.4/0.4/0.2. The challenge attracted 10 teams with 82 participants submitting innovative solutions. The best-performing methods for each individual metric achieved 90.26\% mDSC, 38.88 mHD, and 32.85 ms RT, respectively. FUGC establishes a standardized benchmark for cervical segmentation, demonstrates the efficacy of semi-supervised methods with limited labeled data, and provides a foundation for AI-assisted clinical PTB risk assessment.

