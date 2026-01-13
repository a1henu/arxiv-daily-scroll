---
layout: default
title: PLANET v2.0: A comprehensive Protein-Ligand Affinity Prediction Model Based on Mixture Density Network
---

# PLANET v2.0: A comprehensive Protein-Ligand Affinity Prediction Model Based on Mixture Density Network
**arXiv**：[2601.07415v1](https://arxiv.org/abs/2601.07415) · [PDF](https://arxiv.org/pdf/2601.07415.pdf)  
**作者**：Haotian Gao, Xiangying Zhang, Jingyuan Li, Xinchong Chen, Haojie Wang, Yifei Qi, Renxiao Wang  

**一句话要点**：提出PLANET v2.0以改进蛋白质-配体亲和力预测，通过混合密度网络提升虚拟筛选效率。

**关键词**：蛋白质-配体亲和力预测, 混合密度网络, 虚拟筛选, 多目标训练, 高斯混合模型, 药物发现

## 3 点简述
- 核心问题：PLANET模型在蛋白质-配体接触图表示上存在缺陷，影响亲和力预测准确性。
- 方法要点：采用多目标训练策略和混合密度网络预测结合模式，并创新使用高斯混合模型描述距离-能量关系。
- 实验或效果：在CASF-2016基准测试中表现优异，筛选能力显著提升，并在大规模数据集上验证稳健性。

## 摘要（原文）

> Drug discovery represents a time-consuming and financially intensive process, and virtual screening can accelerate it. Scoring functions, as one of the tools guiding virtual screening, have their precision closely tied to screening efficiency. In our previous study, we developed a graph neural network model called PLANET (Protein-Ligand Affinity prediction NETwork), but it suffers from the defect in representing protein-ligand contact maps. Incorrect binding modes inevitably lead to poor affinity predictions, so accurate prediction of the protein-ligand contact map is desired to improve PLANET. In this study, we have proposed PLANET v2.0 as an upgraded version. The model is trained via multi-objective training strategy and incorporates the Mixture Density Network to predict binding modes. Except for the probability density distributions of non-covalent interactions, we innovatively employ another Gaussian mixture model to describe the relationship between distance and energy of each interaction pair and predict protein-ligand affinity like calculating the mathematical expectation. As on the CASF-2016 benchmark, PLANET v2.0 demonstrates excellent scoring power, ranking power, and docking power. The screening power of PLANET v2.0 gets notably improved compared to PLANET and Glide SP and it demonstrates robust validation on a commercial ultra-large-scale dataset. Given its efficiency and accuracy, PLANET v2.0 can hopefully become one of the practical tools for virtual screening workflows. PLANET v2.0 is freely available at https://www.pdbbind-plus.org.cn/planetv2.

