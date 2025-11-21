---
layout: default
title: Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations
---

# Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations
**arXiv**：[2511.16661v1](https://arxiv.org/abs/2511.16661) · [PDF](https://arxiv.org/pdf/2511.16661.pdf)  
**作者**：Irmak Guzey, Haozhi Qi, Julen Urain, Changhao Wang, Jessica Yin, Krishna Bodduluri, Mike Lambeta, Lerrel Pinto, Akshara Rai, Jitendra Malik, Tingfan Wu, Akash Sharma, Homanga Bharadhwaj  

**一句话要点**：提出AINA框架，从智能眼镜采集的人类演示中学习多指机器人操作策略

**关键词**：多指机器人操作, 人类演示学习, 智能眼镜数据采集, 3D点策略, 野外视频学习, 机器人策略泛化

## 3 点简述
- 核心问题：人类与机器人间的具身差距及从野外视频提取运动线索的困难阻碍了机器人策略学习
- 方法要点：使用Aria Gen 2眼镜采集数据，结合3D头部和手部姿态，学习基于3D点的多指策略
- 实验或效果：在九个日常操作任务中验证，策略对背景变化鲁棒，无需机器人数据即可部署

## 摘要（原文）

> Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

