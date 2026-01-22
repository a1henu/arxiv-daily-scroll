---
layout: default
title: RegFreeNet: A Registration-Free Network for CBCT-based 3D Dental Implant Planning
---

# RegFreeNet: A Registration-Free Network for CBCT-based 3D Dental Implant Planning
**arXiv**：[2601.14703v1](https://arxiv.org/abs/2601.14703) · [PDF](https://arxiv.org/pdf/2601.14703.pdf)  
**作者**：Xinquan Yang, Xuguang Li, Mianjie Zheng, Xuefen Liu, Kun Tang, Kian Ming Lim, He Meng, Jianfeng Ren, Linlin Shen  

**一句话要点**：提出RegFreeNet以解决CBCT三维牙种植规划中依赖配准和配对数据的问题

**关键词**：牙种植规划, CBCT图像处理, 无配准学习, 三维分割, 斜率感知网络, 多中心数据集

## 3 点简述
- 核心问题：现有方法需配准术后数据获取种植体标签，过程耗时且依赖配准精度，多中心数据集构建受限。
- 方法要点：通过掩码术后数据中的种植体，无需配准即可利用任何含种植体的CBCT数据训练，并设计斜率感知网络预测种植位置。
- 实验或效果：在ImplantFairy和两个公共数据集上验证，RegFreeNet达到最先进性能，并发布大规模公开数据集。

## 摘要（原文）

> As the commercial surgical guide design software usually does not support the export of implant position for pre-implantation data, existing methods have to scan the post-implantation data and map the implant to pre-implantation space to get the label of implant position for training. Such a process is time-consuming and heavily relies on the accuracy of registration algorithm. Moreover, not all hospitals have paired CBCT data, limitting the construction of multi-center dataset. Inspired by the way dentists determine the implant position based on the neighboring tooth texture, we found that even if the implant area is masked, it will not affect the determination of the implant position. Therefore, we propose to mask the implants in the post-implantation data so that any CBCT containing the implants can be used as training data. This paradigm enables us to discard the registration process and makes it possible to construct a large-scale multi-center implant dataset. On this basis, we proposes ImplantFairy, a comprehensive, publicly accessible dental implant dataset with voxel-level 3D annotations of 1622 CBCT data. Furthermore, according to the area variation characteristics of the tooth's spatial structure and the slope information of the implant, we designed a slope-aware implant position prediction network. Specifically, a neighboring distance perception (NDP) module is designed to adaptively extract tooth area variation features, and an implant slope prediction branch assists the network in learning more robust features through additional implant supervision information. Extensive experiments conducted on ImplantFairy and two public dataset demonstrate that the proposed RegFreeNet achieves the state-of-the-art performance.

