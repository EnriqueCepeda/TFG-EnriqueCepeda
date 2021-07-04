
export const getBuildings = state => {
    var filteredItems = {};
    Object.keys(state.buildings).map((dictkey) => {
        if (dictkey !== "grid agent") {
            filteredItems[dictkey] = state.buildings[dictkey];
        }
    })
    return filteredItems;


}

export const getBuilding = (state, ol_uid) => getBuildings(state)[ol_uid]

export const getConsumerBuildings = (state) => {
    const buildings = getBuildings(state);
    var filteredItems = {};
    Object.keys(buildings).map((dictkey) => {
        if (buildings[dictkey].type !== "Producer") {
            filteredItems[dictkey] = buildings[dictkey];
        }
    })
    return filteredItems;
}


export const getProducerBuildings = (state) => {
    const buildings = getBuildings(state);
    var filteredItems = {};
    Object.keys(buildings).map((dictkey) => {
        if (buildings[dictkey].type !== "Consumer") {
            filteredItems[dictkey] = buildings[dictkey];
        }
    })
    return filteredItems;
}

export const getBuildingConsumption = (state, building_id) => {
    const buildings = getBuildings(state);
    return buildings[building_id].consumption
}