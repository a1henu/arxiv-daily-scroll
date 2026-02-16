---
layout: default
title: Beyond Benchmarks of IUGC: Rethinking Requirements of Deep Learning Methods for Intrapartum Ultrasound Biometry from Fetal Ultrasound Videos
---

# Beyond Benchmarks of IUGC: Rethinking Requirements of Deep Learning Methods for Intrapartum Ultrasound Biometry from Fetal Ultrasound Videos
**arXiv**：[2602.12922v1](https://arxiv.org/abs/2602.12922) · [PDF](https://arxiv.org/pdf/2602.12922.pdf)  
**作者**：Jieyun Bai, Zihao Zhou, Yitong Tang, Jie Gan, Zhuonan Liang, Jianan Fan, Lisa B. Mcguire, Jillian L. Clarke, Weidong Cai, Jacaueline Spurway, Yubo Tang, Shiye Wang, Wenda Shen, Wangwang Yu, Yihao Li, Philippe Zhang, Weili Jiang, Yongjie Li, Salem Muhsin Ali Binqahal Al Nasim, Arsen Abzhanov, Numan Saeed, Mohammad Yaqub, Zunhui Xian, Hongxing Lin, Libin Lan, Jayroop Ramesh, Valentin Bacher, Mark Eid, Hoda Kalabizadeh, Christian Rupprecht, Ana I. L. Namburete, Pak-Hei Yeung, Madeleine K. Wyburd, Nicola K. Dinsdale, Assanali Serikbey, Jiankai Li, Sung-Liang Chen, Zicheng Hu, Nana Liu, Yian Deng, Wei Hu, Cong Tan, Wenfeng Zhang, Mai Tuyet Nhi, Gregor Koehler, Rapheal Stock, Klaus Maier-Hein, Marawan Elbatel, Xiaomeng Li, Saad Slimani, Victor M. Campello, Benard Ohene-Botwe, Isaac Khobo, Yuxin Huang, Zhenyan Han, Hongying Hou, Di Qiu, Zheng Zheng, Gongning Luo, Dong Ni, Yaosheng Lu, Karim Lekadir, Shuo Li  

**一句话要点**：提出多任务自动测量框架与大型数据集，以支持资源有限环境下的产时超声生物测量

**关键词**：产时超声生物测量, 多任务学习, 超声视频分析, 临床挑战赛, 资源有限医疗

## 3 点简述
- 核心问题：产时阶段母婴死亡率高，但资源有限地区缺乏训练有素的超声医师，阻碍超声常规应用。
- 方法要点：设计多任务框架，集成标准平面分类、胎儿头-耻骨联合分割和生物测量，利用任务互补性提升准确性。
- 实验或效果：发布最大多中心产时超声视频数据集，分析八支团队方法，识别瓶颈并公开解决方案促进研究。

## 摘要（原文）

> A substantial proportion (45\%) of maternal deaths, neonatal deaths, and stillbirths occur during the intrapartum phase, with a particularly high burden in low- and middle-income countries. Intrapartum biometry plays a critical role in monitoring labor progression; however, the routine use of ultrasound in resource-limited settings is hindered by a shortage of trained sonographers. To address this challenge, the Intrapartum Ultrasound Grand Challenge (IUGC), co-hosted with MICCAI 2024, was launched. The IUGC introduces a clinically oriented multi-task automatic measurement framework that integrates standard plane classification, fetal head-pubic symphysis segmentation, and biometry, enabling algorithms to exploit complementary task information for more accurate estimation. Furthermore, the challenge releases the largest multi-center intrapartum ultrasound video dataset to date, comprising 774 videos (68,106 frames) collected from three hospitals, providing a robust foundation for model training and evaluation. In this study, we present a comprehensive overview of the challenge design, review the submissions from eight participating teams, and analyze their methods from five perspectives: preprocessing, data augmentation, learning strategy, model architecture, and post-processing. In addition, we perform a systematic analysis of the benchmark results to identify key bottlenecks, explore potential solutions, and highlight open challenges for future research. Although encouraging performance has been achieved, our findings indicate that the field remains at an early stage, and further in-depth investigation is required before large-scale clinical deployment. All benchmark solutions and the complete dataset have been publicly released to facilitate reproducible research and promote continued advances in automatic intrapartum ultrasound biometry.

