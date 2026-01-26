---
layout: default
title: LongCat-Flash-Thinking-2601 Technical Report
---

# LongCat-Flash-Thinking-2601 Technical Report
**arXiv**：[2601.16725v1](https://arxiv.org/abs/2601.16725) · [PDF](https://arxiv.org/pdf/2601.16725.pdf)  
**作者**：Meituan LongCat Team, Anchun Gui, Bei Li, Bingyang Tao, Bole Zhou, Borun Chen, Chao Zhang, Chao Zhang, Chen Gao, Chen Zhang, Chengcheng Han, Chenhui Yang, Chuyu Zhang, Cong Chen, Cunguang Wang, Daoru Pan, Defei Bu, Dengchang Zhao, Di Xiu, Dishan Liu, Dongyu Ru, Dunwei Tu, Fan Wu, Fengcheng Yuan, Fengcun Li, Gang Xu, Guanyu Wu, Guoyuan Lin, Haibin Wang, Hansi Yang, Hao Yang, Haonan Yan, Haoxiang Ma, Haoxing Wen, Hongyan Hao, Hongyin Tang, Hongyu Zang, Hongzhi Ni, Hui Su, Jiacheng Zhang, Jiahong Zhou, Jiahuan Li, Jiaming Wang, Jian Yang, Jianfei Zhang, Jianhao Xu, Jianing Wang, Jiapeng Zhu, Jiaqi Sun, Jiarong Shi, Jiarui Zhao, Jingang Wang, Jinluan Yang, Jinrui Ding, Jinwei Xiao, Jiyuan He, Juncan Xu, Kefeng Zhang, Keheng Wang, Li Wei, Lianhui Ma, Lin Qiu, Lingbing Kong, Lingchuan Liu, Linsen Guo, Mengshen Zhu, Mengxia Shen, Mingyang Zhu, Peiguang Li, Peng Pei, Pengcheng Jia, Pengtao Zhang, Peng Zhao, Qi Gu, Qiong Huang, Qiyuan Duan, Quanchi Weng, Rongxiang Weng, Rongzhi Zhang, Rumei Li, Shanglin Lei, Shengnan An, Shijun Dai, Shuaikang Liu, Shuang Zhou, Shuo Wang, Songyuan Zhao, Tao Liang, Tianhao Hu, Tianze Chen, Wei Liu, Wei Shi, Wei Wang, Weifeng Tang, Wenjie Shi, Wenlong Zhu, Wentao Chen, Wentao Shi, Xi Su, Xiangcheng Liu, Xiandi Ma, Xiangyu Xi, Xiangyuan Liu, Xiangzhou Huang, Xiao Liu, Xiaodong Cai, Xiaolong Chen, Xiaowei Shi, Xiaoyu Li, Xin Chen, Xingchen Liu, Xuan Huang, Xuezhi Cao, Xunliang Cai, Yan Chen, Yang Bai, Yang Liu, Yang Yang, Yang Zheng, Yaoming Wang, Yaoming Zhu, Yaqi Huo, Yanyu Chen, Yaorui Shi, Yerui Sun, Yi Zhang, Yihao Chen, Yi-Kai Zhang, Yifan Lu, Yifan Zhao, Yitao Zhai, Yongjing Yin, Yongwei Zhou, Youshao Xiao, Yuchuan Dai, Yuchen Xie, Yuchen Yu, Yufei Zhang, Yuhuai Wei, Yulei Qian, Yunfan Liang, Yunke Zhao, Yuwei Jiang, Yuxin Bian, Yuxin Chen, Yuxin Liu, Yue Xu, Yueqing Sun, Zeyang Yu, Zhao Yang, Zhengsheng Huang, Zhengyu Chen, Zhijian Liu, Zhikang Xia, Zhimin Lin, Zhiyuan Yao, Zhuofan Chen, Zhuowen Han, Zijian Zhang, Ziran Li, Ziwen Wang, Ziyuan Zhuang  

**一句话要点**：提出5600亿参数开源MoE推理模型LongCat-Flash-Thinking-2601，以提升智能体推理能力

**关键词**：混合专家模型, 智能体推理, 异步强化学习, 工具使用, 鲁棒性训练, 大规模训练

## 3 点简述
- 核心问题：提升开源模型在智能体搜索、工具使用等复杂推理任务中的性能与泛化能力
- 方法要点：采用统一训练框架，结合领域并行专家训练与融合，并系统扩展异步强化学习框架DORA以支持大规模多环境训练
- 实验或效果：在多种智能体基准测试中达到开源模型最优，并展示了对复杂工具交互和噪声环境的强鲁棒性

## 摘要（原文）

> We introduce LongCat-Flash-Thinking-2601, a 560-billion-parameter open-source Mixture-of-Experts (MoE) reasoning model with superior agentic reasoning capability. LongCat-Flash-Thinking-2601 achieves state-of-the-art performance among open-source models on a wide range of agentic benchmarks, including agentic search, agentic tool use, and tool-integrated reasoning. Beyond benchmark performance, the model demonstrates strong generalization to complex tool interactions and robust behavior under noisy real-world environments. Its advanced capability stems from a unified training framework that combines domain-parallel expert training with subsequent fusion, together with an end-to-end co-design of data construction, environments, algorithms, and infrastructure spanning from pre-training to post-training. In particular, the model's strong generalization capability in complex tool-use are driven by our in-depth exploration of environment scaling and principled task construction. To optimize long-tailed, skewed generation and multi-turn agentic interactions, and to enable stable training across over 10,000 environments spanning more than 20 domains, we systematically extend our asynchronous reinforcement learning framework, DORA, for stable and efficient large-scale multi-environment training. Furthermore, recognizing that real-world tasks are inherently noisy, we conduct a systematic analysis and decomposition of real-world noise patterns, and design targeted training procedures to explicitly incorporate such imperfections into the training process, resulting in improved robustness for real-world applications. To further enhance performance on complex reasoning tasks, we introduce a Heavy Thinking mode that enables effective test-time scaling by jointly expanding reasoning depth and width through intensive parallel thinking.

